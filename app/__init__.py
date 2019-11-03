import os
from flask import Flask
from peewee import SqliteDatabase
from dotenv import load_dotenv

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(APP_ROOT, 'forecasts.db')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.from_object(__name__)

db = SqliteDatabase(app.config['DATABASE'], pragmas={
    'journal_mode': 'wal',  # WAL-mode for better concurrent access.
    'cache_size': -32000})  # 32MB page cache.

from app import views
from app import models
