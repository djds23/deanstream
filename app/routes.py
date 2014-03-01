from flask import Flask, render_template, jsonify, request, g, url_for
from app import app
import random
import models
import collections

@app.route('/')
def home():
    '''creates the dict with the filepaths, and returns the template'''
    new_video()
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/_new_video')
def new_video():
    current_id = request.args.get('current_id')
    videos = models.Video.query.all()
    pool = [video for video in videos if video != current_id]
    print type(random.choice(pool))
    #new_video = models.Video.query.get(random.choice(pool))
    #webm = new_video.get_webm()
    #mp4 = new_video.get_mp4()
    return #jsonify(webm=webm,mp4=mp4,video_id=video_id)
