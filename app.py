from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    user={
        "nombre":"Luz",
        "apellido":"Vivanco",
        "telefono":"999999"
    }
    
    #return render_template("index.html",
    #    nombre=user["nombre"],
    #    apellido=user["apellido"],
    #    telefono=user["telefono"]                      
    #)
                           
    return render_template("index.html",**user) #con **user estamos descomprimiendo ese diccionario

@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Esta es una ruta nueva sin HTML"

@app.route('/ruta-nueva-1/ruta_html')
def ruta_nueva_html():
    return render_template("nuevo.html")