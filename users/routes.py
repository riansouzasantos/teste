from users import app
from .models import Usuario
from flask import Flask, render_template

@app.route('/')
def user():
    with app.app_context():
        usuario = Usuario.query.all()
    return render_template('User.html', usuario=usuario)



