from flask import render_template,flash,redirect,url_for,session
from flask_bcrypt import Bcrypt
from app import create_app
from app.forms import SalonesForm,LoginForm,RegisterForm
from app.db import db

from app.models.salones import Salon
from app.models.user import User

app=create_app()
bcrypt=Bcrypt(app) #instancia

@app.route('/',methods=["GET","POST"])
def index():
    if 'user_id' in session:
        return redirect(url_for('blog'))
    
    login_form = LoginForm() #instanciamos

    if login_form.validate_on_submit():
        #1. Recuperar al usuario por correo
        user=User.query.filter_by(correo=login_form.email.data).first()

        if user is not None:
            #2. Encriptar el password que esta como texto para compararlo con el de la base de datos
            if bcrypt.check_password_hash(user.password,login_form.password.data):
                flash('Datos correctos','success')

                session['user_id']=user.id

                #3.Redirigirlo hacia otra vista
                return redirect(url_for('blog'))
            else:
                flash('Datos erroneos','error')

    return render_template("login.html",login_form=login_form)

@app.route('/register',methods=["GET","POST"])
def register():
    if 'user_id' in session:
        return redirect(url_for('blog'))
    
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        user=User(
            register_form.nombre.data,
            register_form.apellido.data,
            register_form.correo.data,
            bcrypt.generate_password_hash(register_form.password.data),
            register_form.sobre_mi.data
        )

        #con esto guardamos al usuario
        db.session.add(user)
        db.session.commit()

        flash("Usuario creado correctamente","success")

        return redirect(url_for('index'))
    
    return render_template("register.html",register_form=register_form)

@app.route('/blog')
def blog():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('blog.html')

""" @app.route('/',methods=['GET','POST'])
def index():
    salones_form=SalonesForm()  #instanciamos el objeto 

    if salones_form.validate_on_submit():  
        salon=Salon(
            salones_form.aula.data,
            salones_form.horaEntrada.data,
        )

        db.session.add(salon)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("salones.html",salones_form=salones_form) """ #con **user estamos descomprimiendo ese diccionario

@app.route('/salones')
def salones():
    salones=Salon.query.all()

    return render_template("lista-salones.html",salones=salones)

@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Esta es una ruta nueva sin HTML"

@app.route('/ruta-nueva-1/ruta_html')
def ruta_nueva_html():
    return render_template("nuevo.html")

#crean automaticamente las migraciones
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)