from flask import render_template
from app import create_app
from app.forms import SalonesForm

app=create_app()

@app.route('/')
def index():
    salones_form=SalonesForm()  #instanciamos el objeto              
    return render_template("salones.html",salones_form=salones_form) #con **user estamos descomprimiendo ese diccionario

@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Esta es una ruta nueva sin HTML"

@app.route('/ruta-nueva-1/ruta_html')
def ruta_nueva_html():
    return render_template("nuevo.html")