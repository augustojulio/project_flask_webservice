from app import app, db
from sqlalchemy import Column, Integer, String, DateTime

class Forecast(db.Model):
    __tablename__ = 'forecasts'
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(128), unique=True, nullable=False)
    estado = db.Column(db.String(128), unique=True, nullable=False)
    pais = db.Column(db.String(128), unique=True, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    probabilidade = db.Column(Integer, unique=True, nullable=False)
    precipitacao = db.Column(Integer, unique=True, nullable=False)
    temperatura_min = db.Column(Integer, unique=True, nullable=False)
    temperatura_max = db.Column(Integer, unique=True, nullable=False)
