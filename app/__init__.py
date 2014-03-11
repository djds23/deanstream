from flask import Flask, render_template, jsonify, request, g, url_for, session
from key_gen  import return_uuid
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = return_uuid()
db = SQLAlchemy(app)

from app import routes, models
