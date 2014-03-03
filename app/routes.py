from flask import Flask, render_template, jsonify, request, g, url_for
from app import app
from randomizer import gen_random_video
import models


videos = [_ for _ in range(models.Video.query.count()+1) if models.Video.query.get(_) != None ]
recently_watched_generator = gen_random_video(videos)

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
    video_id = next(recently_watched_generator)
    new_video = models.Video.query.get(video_id)
    webm = new_video.get_webm()
    mp4 = new_video.get_mp4()
    print video_id
    return jsonify(webm=webm,mp4=mp4,video_id=video_id)
