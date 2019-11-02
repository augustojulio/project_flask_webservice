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


