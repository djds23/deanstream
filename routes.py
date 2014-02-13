from flask import Flask, render_template, jsonify, request
import random
import os

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:8000'

@app.route('/')
def home(altimg=None):
    agent = r:quest.headers.get('User-Agent')
    if ('iphone' or 'android' or 'blackberry') in agent.lower():
         return render_template('index.html', altimg='static/img/mobile.jpg')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/_new_video')
def new_video():
    current_video = request.args.get('current_video')
    videos =[video for video in  os.listdir('static/webm/') if
            video[-5:]=='.webm' and video not in current_video]
    return jsonify(stream=random.choice(videos))

if __name__ == '__main__':
    app.run(debug=True)
