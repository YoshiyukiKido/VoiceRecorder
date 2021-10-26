#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import os
import datetime

ALLOWED_EXTENSIONS = set(['jpg', 'avi', 'mp4', 'webm', 'wav'])

app = Flask(__name__)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    fname = "uploads/" + datetime.datetime.now().strftime('%m%d%H%M%S') + ".wav"
    with open(f"{fname}", "wb") as f:
        f.write(request.files['audio_data'].read())
    print(f"posted sound file: {fname}")
    return render_template('index.html', request="POST")   


if __name__ == "__main__":
    app.debug=True
    app.threaded=True
    app.run(host='0.0.0.0', ssl_context=('cert/server.crt', 'cert/server.key'))

