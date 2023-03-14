from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    nombre="Luz Vivanco"
    return render_template("index.html",nombre=nombre)

@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Esta es una ruta nueva sin HTML"

@app.route('/ruta-nueva-1/ruta_html')
def ruta_HTML():
    return render_template("ruta.html")