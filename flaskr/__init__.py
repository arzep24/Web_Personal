from flask import Flask

App = Flask(__name__)

#Importgando y Registrando el Blueprint "Vista" base para poder ver todas las "vistas" creqadas en la aplicacion base de la web personal
from flaskr.views import base
App.register_blueprint(base)