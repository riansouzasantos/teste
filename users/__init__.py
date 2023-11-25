from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = '21aceda4d8254352b47a4b407cd54c7f'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
# database = SQLAlchemy(app)

if os.getenv('DATABASE_URL'): 
   app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'

database = SQLAlchemy(app)

from users import routes