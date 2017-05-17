import uuid

from flask import Flask, render_template, jsonify, request, g, url_for, session
from flask_sqlalchemy import SQLAlchemy


def return_uuid():
    '''return a string with your secret key'''
    key = uuid.uuid1()
    return str(key)

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = return_uuid()
db = SQLAlchemy(app)

from . import routes, models
