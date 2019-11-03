from app import app
from app import models
from flask import request, jsonify
import requests

@app.route("/city")
# example: localhost:5000/city?id=<ID_DA_CIDADE>
def city():
    id_city = request.args.get('id')
    token = 'b22460a8b91ac5f1d48f5b7029891b53'

    url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{0}/days/15?token={1}'.format(id_city, token)
    forecast = requests.get(url).json()
    for i in forecast["data"]:
        # print(forecast["id"])
        # print(forecast["name"])
        # print(forecast["state"])
        # print(forecast["country"])
        # print(i["date_br"])
        # print(i["rain"]["probability"])
        # print(i["rain"]["precipitation"])
        # print(i["temperature"]["min"])
        # print(i["temperature"]["max"])

        forecast1 = models.Forecast.create(cidade=forecast["name"], estado=forecast["state"], pais=forecast["country"], data=i["date_br"], probabilidade=i["rain"]["probability"], precipitacao=i["rain"]["precipitation"], temperatura_min=i["temperature"]["min"], temperatura_max=i["temperature"]["max"])
        forecast1.save()

    return '', 204

@app.route("/analysis")
# example: localhost:5000/analysis?data_inicial=02/11/2019&data_final=05/11/2019
def analysis():
    initial_date = request.args.get('data_inicial')
    final_date = request.args.get('data_final')
    print(initial_date)
    print(final_date)

    forecasts2 = models.Forecast.select()
    for forecast2 in forecasts2:
        print('{} , {} , {} , {}'.format(forecast2.cidade, forecast2.data, forecast2.temperatura_max, forecast2.precipitacao))
        # print('{} on {}'.format(note.text, note.created))

    return "read info from db"