from app import app
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime

# class Forecast(db.Model):
#     __tablename__ = 'forecasts'
#     id = db.Column(db.Integer, primary_key=True)
#     cidade = db.Column(db.String(128), unique=True, nullable=False)
#     estado = db.Column(db.String(128), unique=True, nullable=False)
#     data = db.Column(db.DateTime, nullable=False)
#     probabilidade = db.Column(Integer, unique=True, nullable=False)
#     precipitacao = db.Column(Integer, unique=True, nullable=False)
#     temperatura_min = db.Column(Integer, unique=True, nullable=False)
#     temperatura_max = db.Column(Integer, unique=True, nullable=False)
#     pais = db.Column(db.String(128), unique=True, nullable=False)


metadata = MetaData()
forecasts = Table('forecasts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('cidade', String(128), nullable=False),
    Column('estado', String(128), nullable=False),
    Column('data', DateTime, nullable=False),
    Column('probabilidade', Integer(), nullable=False),
    Column('precipitacao', Integer(), nullable=False),
    Column('temperatura_min', Integer(), nullable=False),
    Column('temperatura_max', Integer(), nullable=False),
    Column('pais', String(128), nullable=False),
)

