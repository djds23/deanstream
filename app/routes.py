from flask import Flask, render_template, jsonify, request, g, url_for, session
from app import app
from randomizer import Randomizer
import models

@app.route('/')
def home():
    '''creates the dict with the filepaths, and returns the template'''
    if session.new:    
        app.open_session(request)    
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
    video_id = next(Randomizer().gen_random_video())
    new_video = models.Video.query.get(video_id)
    webm = new_video.get_webm()
    mp4 = new_video.get_mp4()
    return jsonify(webm=webm,mp4=mp4,video_id=video_id)
