from app import app, db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db

class Forecast(BaseModel):
    cidade = CharField()
    estado = CharField()
    pais = CharField()
    data = DateTimeField()
    probabilidade = IntegerField()
    precipitacao = IntegerField()
    temperatura_min = IntegerField()
    temperatura_max = IntegerField()

# forecast1 = Forecast.create(cidade='Araraquara', estado='sp', pais='br', data='sss', probabilidade=2, precipitacao=1, temperatura_min=23, temperatura_max=35)
# forecast1.save()

