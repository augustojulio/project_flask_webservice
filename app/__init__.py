import os
from flask import Flask
# from peewee import SqliteDatabase
from flask_sqlalchemy_core import FlaskSQLAlchemy
from dotenv import load_dotenv
# from sqlalchemy import create_engine
# engine = create_engine

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
# DATABASE = os.path.join(APP_ROOT, 'forecasts.db')
DATABASE_URL = "postgresql://localhost/forecasts"
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.from_object(__name__)

# db = SqliteDatabase(app.config['DATABASE'], pragmas={
#     'journal_mode': 'wal',  # WAL-mode for better concurrent access.
#     'cache_size': -32000})  # 32MB page cache.

db = FlaskSQLAlchemy(DATABASE_URL)

from app import views
from app import models
