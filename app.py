#!/usr/bin/python

from flask import Flask, render_template, request
from readAtten import *

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')

def index():
     
    atten1  = readAtten1()
    atten2  = readAtten2()
    atten3  = readAtten3()
    atten4  = readAtten4()
    atten5  = readAtten5()
    atten6  = readAtten6()
    atten7  = readAtten7()
    atten8  = readAtten8()
    atten9  = readAtten9()
    atten10 = readAtten10()
    atten11 = readAtten11()
    atten12 = readAtten12()
    atten13 = readAtten13()
    atten14 = readAtten14()
    atten15 = readAtten15()
    atten16 = readAtten16()
      
    return render_template('index.html', attens1=atten1, attens2=atten2, attens3=atten3, attens4=atten4, attens5=atten5, attens6=atten6, attens7=atten7, attens8=atten8, 
    	attens9=atten9, attens10=atten10, attens11=atten11, attens12=atten12, attens13=atten13, attens14=atten14, attens15=atten15, attens16=atten16)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=int("8080"))
