from flask import Flask, render_template, jsonify, request
from random import randint
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/_new_video')
def new_video():
    videos =[video for video in  os.listdir('static/webm/') if
            video[-5:]=='.webm']
    return jsonify(stream=videos[randint(0,1)])

if __name__ == '__main__':
    app.run(debug=True)
