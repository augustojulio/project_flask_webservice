from app import app
from app import models
from flask import render_template, request, jsonify
import requests

@app.route("/")
def index():
	return "Para testar, por favor acesse a seguinte rota segundo o exemple: localhost:5000/city?id=ID_DA_CIDADE. Sendo id=3477 para cidade de São Paulo"

@app.route('/city')
# example: localhost:5000/cidade?id=<ID_DA_CIDADE>
def city():
    id_city = request.args.get('id')
    token = 'b22460a8b91ac5f1d48f5b7029891b53'

    # print(id_city)
    # print(token)

    url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{0}/days/15?token={1}'.format(id_city, token)
    forecast = requests.get(url).json()
    # print(forecast["id"])
    # print(forecast["name"])
    # print(forecast["state"])
    # print(forecast["country"])
    for i in forecast["data"]:
        print(forecast["id"])
        print(forecast["name"])
        print(forecast["state"])
        print(forecast["country"])
        print(i["date_br"])
        print(i["rain"]["probability"])
        print(i["rain"]["precipitation"])
        print(i["temperature"]["min"])
        print(i["temperature"]["max"])

        forecast1 = models.Forecast.create(cidade=forecast["name"], estado=forecast["state"], pais=forecast["country"], data=i["date_br"], probabilidade=i["rain"]["probability"], precipitacao=i["rain"]["precipitation"], temperatura_min=i["temperature"]["min"], temperatura_max=i["temperature"]["max"])
        forecast1.save()

    # forecast1 = models.Forecast.create(cidade=forecast["name"], estado=forecast["state"], pais=forecast["country"], data='aaa', probabilidade=3, precipitacao=3, temperatura_min=33, temperatura_max=38)
    # forecast1.save()

    return jsonify(forecast)

