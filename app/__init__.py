import os
from flask import Flask
from peewee import SqliteDatabase

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(APP_ROOT, 'forecasts.db')

app = Flask(__name__)
app.config.from_object(__name__)

db = SqliteDatabase(app.config['DATABASE'], pragmas={
    'journal_mode': 'wal',  # WAL-mode for better concurrent access.
    'cache_size': -32000})  # 32MB page cache.

from app import views
from app import models