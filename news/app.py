#!/usr/bin/env python3

from flask import Flask,render_template
import os,json

app = Flask(__name__)

@app.route('/')
def index():
    path = "/home/shiyanlou/files/"
    dirs = os.listdir(path)
    data = []
    for file in dirs:
        file = path+file
        with open(file,'r') as f:
            data.append(json.load(f))
    return render_template('index.html',data=data)

@app.route('/files/<filename>')
def file(filename):
    path = "/home/shiyanlou/files/"
    filename = path+filename
    if filename not in ['/home/shiyanlou/files/helloshiyanlou','/home/shiyanlou/files/helloworld']:
        return render_template('404.html')
    else:
        filename = filename+'.json'
        with open(filename,'r') as f:
            data = json.load(f)
        return render_template('file.html',data=data)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__=='__main__':
    app.run()
