import os
from flask import Flask
from dotenv import load_dotenv

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
