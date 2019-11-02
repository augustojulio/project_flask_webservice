from app import app
from app import models
from flask import render_template, request, jsonify
import requests


print(models.Forecast)

forecast1 = models.Forecast.create(cidade='Sao Carlos', estado='sp', pais='br', data='aaa', probabilidade=3, precipitacao=3, temperatura_min=33, temperatura_max=38)
forecast1.save()

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

    return jsonify(forecast)


