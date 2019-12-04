"""
views module
"""
import os
from app import app
from app import models
from flask import request, jsonify
from sqlalchemy import func, create_engine
import requests
from sqlalchemy.sql import select

try:
    engine = create_engine('postgresql://augusto:123456@localhost/forecasts')
    conn = engine.connect()
    print("Connected to DB with core")
except ConnectionError:
    print("Problem to connect DB with core")


# Example: localhost:5000/city?id=<ID_DA_CIDADE>
@app.route("/city")
def city():
    id_city = request.args.get('id')
    token = os.getenv("TOKEN")

    url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{0}' \
          '/days/15?token={1}'.format(id_city, token)
    forecast = requests.get(url).json()
    for i in forecast["data"]:

        forecast1 = models.forecasts.insert().values(
            id='3',
            cidade=forecast["name"],
            estado=forecast["state"],
            data=i["date_br"],
            probabilidade=i["rain"]["probability"],
            precipitacao=i["rain"]["precipitation"],
            temperatura_min=i["temperature"]["min"],
            temperatura_max=i["temperature"]["max"],
            pais=forecast["country"],)
        conn.execute(forecast1)

    return '', 204

# Example:
# localhost:5000/analysis?data_inicial=02/11/2019&data_final=05/11/2019
@app.route("/analysis")
def analysis():
    initial_date = request.args.get('data_inicial')
    final_date = request.args.get('data_final')

    list_results = []

    '''forecasts_max = select([models.forecasts.c.cidade, models.forecasts.c.data,
    func.max(models.forecasts.c.temperatura_max)]).
    where(models.forecasts.c.data.between(initial_date, final_date))'''
    forecasts_max = select([models.forecasts])
    result = conn.execute(forecasts_max)
    print(result)
    # for forecast_max in forecasts_max:
    for forecast_max in result:
        list_results.append(
            'A cidade com maior temperatura máxima no período espeficado é: {}'
            .format(forecast_max.cidade))
        print(list_results)

    '''forecasts_avg = db.session.query(models.Forecast.cidade,
     models.Forecast.data, func.avg(models.Forecast.precipitacao)
     .alias('avg_precipitacao'))
     .where(models.Forecast.data.between(initial_date, final_date))
     .group_by(models.Forecast.cidade)
    for forecast_avg in forecasts_avg:
        list_results.append('A média de precipitação da cidade de {} é {}'
        .format(forecast_avg.cidade, forecast_avg.avg_precipitacao))

    list_results_string = '\n'.join(list_results)

    return list_results_string'''
    return '', 204
