"""
app module
"""
import os
from flask import Flask
from dotenv import load_dotenv


APP_ROOT = os.path.dirname(os.path.realpath(__file__))

DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)

app = Flask(__name__)
app.config.from_object(__name__)

from app import views
from app import models
