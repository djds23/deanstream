from flask import Flask, render_template, jsonify, request, g, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import random
import os
import models

app = Flask(__name__)
config = app.config.from_object('config')

@app.route('/')
def home():
    '''creates the dict with the filepaths, and returns the template'''
    agent = request.headers.get('User-Agent')
    webm = 'webm/couch.webm'
    mp4 = 'mp4/couch.mp4'
    return render_template('video.html', webm=webm, mp4=mp4)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/_new_video')
def new_video():
    current_video = request.args.get('current_video')
    asset = models.Video.query.order_by('?').limit(1)
    webm = models.Video.query.get(2).get_webm()
    mp4 = models.Video.query.get(2).get_mp4()
    return jsonify(webm=webm,mp4=mp4)

if __name__ == '__main__':
    app.run(debug=True)
