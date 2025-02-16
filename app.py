from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e8f7d9c0b1a2f3e4d5c6b7a8f9e0d1c2e3f4d5c6b7a8f9e0d1c2e3f4d5c6b7a8f9e0d1c2'

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'danielportfolio073@gmail.com'  # Tu correo electrónico
app.config['MAIL_PASSWORD'] = 'knbe ainh miiw wsqw'  # Contraseña o clave de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'danielportfolio073@gmail.com'  # Remitente por defecto
mail = Mail(app)

# Formulario de contacto
class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Crear el mensaje de correo electrónico
            msg = Message(
                subject="Nuevo mensaje de contacto desde tu portfolio",
                recipients=["danielportfolio073@gmail.com"],  # Correo al que se enviará el mensaje
                body=f"Nombre: {form.name.data}\nEmail: {form.email.data}\nMensaje: {form.message.data}"
            )
            mail.send(msg)
            flash('¡Mensaje enviado correctamente!', 'success')
            return redirect(url_for('index'))  # Redirigir al inicio después de enviar
        except Exception as e:
            print(f"Error al enviar el correo: {e}")  # Imprime el error en la consola
            flash('Error al enviar el mensaje. Inténtalo de nuevo más tarde.', 'danger')
    
    # Renderizar la plantilla con el formulario
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)