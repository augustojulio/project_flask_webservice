import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import psycopg2

# try:
#     conn = psycopg2.connect("dbname=forecasts user='augusto' password='123456'")
#     print("Connected to DB")
# except:
#     print("Problem to connect DB")

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.from_object(__name__)
# DB_URL = "postgresql://augusto:123456@localhost/forecasts"
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

from app import views
from app import models

