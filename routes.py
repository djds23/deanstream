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
    current_mp4 = request.args.get('current_mp4')
    current_webm = request.args.get('current_webm')
    while True:
        video_id = random.randrange(1,models.Video.query.count() + 1) # adds one to the limit so that it raises above 1
        new_video = models.Video.query.get(video_id)
        test_case = str(new_video)
        if current_mp4.split('/')[-1] in test_case and current_webm.split('/')[-1]:
            webm = new_video.get_webm()
            mp4 = new_video.get_mp4()
            return jsonify(webm=webm,mp4=mp4)

if __name__ == '__main__':
    app.run(debug=True)
