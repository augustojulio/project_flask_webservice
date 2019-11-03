import os
from app import app
from app import models
from flask import request, jsonify
from peewee import *
import requests

@app.route("/city")
# example: localhost:5000/city?id=<ID_DA_CIDADE>
def city():
    id_city = request.args.get('id')
    token = os.getenv("TOKEN")

    url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{0}/days/15?token={1}'.format(id_city, token)
    forecast = requests.get(url).json()
    for i in forecast["data"]:

        forecast1 = models.Forecast.create(cidade=forecast["name"], estado=forecast["state"], pais=forecast["country"], data=i["date_br"], probabilidade=i["rain"]["probability"], precipitacao=i["rain"]["precipitation"], temperatura_min=i["temperature"]["min"], temperatura_max=i["temperature"]["max"])
        forecast1.save()

    return '', 204

@app.route("/analysis")
# example: localhost:5000/analysis?data_inicial=02/11/2019&data_final=05/11/2019
def analysis():
    initial_date = request.args.get('data_inicial')
    final_date = request.args.get('data_final')

    list_results = []

    forecasts_max = models.Forecast.select(models.Forecast.cidade, models.Forecast.data, fn.MAX(models.Forecast.temperatura_max)).where(models.Forecast.data.between(initial_date, final_date))
    for forecast_max in forecasts_max:
        list_results.append('A cidade com maior temperatura máxima no período espeficado é: {}'.format(forecast_max.cidade))

    forecasts_avg = models.Forecast.select(models.Forecast.cidade, models.Forecast.data, fn.AVG(models.Forecast.precipitacao).alias('avg_precipitacao')).where(models.Forecast.data.between(initial_date, final_date)).group_by(models.Forecast.cidade)
    for forecast_avg in forecasts_avg:
        list_results.append('A média de precipitação da cidade de {} é {}'.format(forecast_avg.cidade, forecast_avg.avg_precipitacao))
    
    list_results_string = '\n'.join(list_results)

    return list_results_string