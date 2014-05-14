#!/usr/bin/python

from flask import Flask, render_template, request
from atten import telNetCall 

# Initialize the Flask application
app = Flask(__name__)

# Default route, print user's IP
@app.route('/')

def index():
    
    values = telNetCall()
    
    #return render_template('index.html', attenValue = output)
    return render_template('index.html', attens=values)

if __name__ == '__main__':
    app.debug = True
    app.run(host="205.243.57.130",port=int("8080"))
