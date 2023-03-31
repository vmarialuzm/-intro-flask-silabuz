from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#Instancia a flask, carga la configuración del proyecto
def create_app():
    app=Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    SQLAlchemy(app)
    return app