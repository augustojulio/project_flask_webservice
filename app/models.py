from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime

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

