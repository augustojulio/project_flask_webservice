import os
from app import app
from app import models
from flask import request, jsonify
from sqlalchemy import func, create_engine
import requests
import psycopg2

try:
    engine = create_engine('postgresql://augusto:123456@localhost/forecasts')
    conn = engine.connect()
    print("Connected to DB with core1")
except:
    print("Problem to connect DB with core")

@app.route("/city")
# example: localhost:5000/city?id=<ID_DA_CIDADE>
def city():
    id_city = request.args.get('id')
    token = os.getenv("TOKEN")

    url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{0}/days/15?token={1}'.format(id_city, token)
    forecast = requests.get(url).json()
    for i in forecast["data"]:

        print('---------------------')
        forecast1 = models.forecasts.insert().values(id='3', cidade=forecast["name"], estado=forecast["state"],
                                    data=i["date_br"], probabilidade=i["rain"]["probability"],
                                    precipitacao=i["rain"]["precipitation"],
                                    temperatura_min=i["temperature"]["min"],
                                    temperatura_max=i["temperature"]["max"],
                                    pais=forecast["country"],)
        # print(forecast1)
        conn.execute(forecast1)
        # db.session.add(forecast1)
        # db.session.commit()

    return '', 204

@app.route("/analysis")
# example: localhost:5000/analysis?data_inicial=02/11/2019&data_final=05/11/2019
def analysis():
    initial_date = request.args.get('data_inicial')
    final_date = request.args.get('data_final')

    list_results = []

    # forecasts_max = db.session.query(models.Forecast.cidade, models.Forecast.data, fn.MAX(models.Forecast.temperatura_max)).where(models.Forecast.data.between(initial_date, final_date))
    forecasts_max = db.session.query(models.Forecast.cidade, models.Forecast.data, func.max(models.Forecast.temperatura_max))
    for forecast_max in forecasts_max:
        list_results.append('A cidade com maior temperatura máxima no período espeficado é: {}'.format(forecast_max.cidade))

    forecasts_avg = db.session.query(models.Forecast.cidade, models.Forecast.data, func.avg(models.Forecast.precipitacao).alias('avg_precipitacao')).where(models.Forecast.data.between(initial_date, final_date)).group_by(models.Forecast.cidade)
    for forecast_avg in forecasts_avg:
        list_results.append('A média de precipitação da cidade de {} é {}'.format(forecast_avg.cidade, forecast_avg.avg_precipitacao))

    list_results_string = '\n'.join(list_results)

    return list_results_string