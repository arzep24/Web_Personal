from flask import render_template, Blueprint

#Utilizo el modulo "BluePrint" par poder modularizar las "vistas" en la  aplicacion 
base = Blueprint("base",__name__)

@base.route("/")
@base.route("/home")
def home():
    return render_template("home.html")