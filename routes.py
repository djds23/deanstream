from flask import Flask, render_template, jsonify, request, g, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import random
import os
import models

app = Flask(__name__)
config = app.config.from_object('config')

def format_data(db_size,result):
    '''input a number of units,a database and a list, and return the format with paths'''
    if db_size == 0:
        return result
    else:
        result.append([
                 models.Video.query.get(db_size).get_webm(),
                models.Video.query.get(db_size).get_mp4()
        ])
        format_data(db_size-1,result)

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
    #current_video = request.args.get('current_video')
    db_size = len(models.Video.query.all())
    videos = format_data(db_size,[])
    supply = random.choice(videos)
    return render_template('video.html',webm=suppy[0],mp4=supply[1])

if __name__ == '__main__':
    app.run(debug=True)
