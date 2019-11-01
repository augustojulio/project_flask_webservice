from flask import render_template
from app import app

@app.route('/')
def index():
	return "Para testar, por favor acesse as seguintes rotas: /city"

@app.route('/city')
def city():
	return render_template("city.html")