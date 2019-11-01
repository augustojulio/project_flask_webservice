from flask import render_template
from flask import request
from app import app

@app.route("/")
def index():
	return "Para testar, por favor acesse a seguinte rota segundo o exemple: localhost:5000/city?id=<ID_DA_CIDADE>. id=3477 para cidade de São Paulo"

@app.route('/city')
# example: localhost:5000/cidade?id=<ID_DA_CIDADE>
def success():
    idd = request.args.get('id')
    print(idd)
    return idd

# @app.route("/city", methods=["GET", "POST"])
# def city():
#     if request.form:
#         print(request.form)
#     return render_template("city.html")