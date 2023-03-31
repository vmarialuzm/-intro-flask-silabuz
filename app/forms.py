from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,EmailField
from wtforms.validators import DataRequired

class SalonesForm(FlaskForm):
    aula=StringField("Aula",validators=[DataRequired()])
    horaEntrada=StringField("Hora de Entrada",validators=[DataRequired()])
    submit=SubmitField("Enviar")

class AlumnosForm(FlaskForm):
    nombre=StringField("Nombre",validators=[DataRequired()])
    apellido=StringField("Apellido",validators=[DataRequired()])
    correo=EmailField("Email",validators=[DataRequired()])
    id_aula=StringField("Id Aula",validators=[DataRequired()])