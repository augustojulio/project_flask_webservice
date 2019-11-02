import os
from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)

from app import views
from app import models