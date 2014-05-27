#!/usr/bin/python
from flask import Flask, render_template, request, redirect
import sys
sys.path.insert(0,'scripts/')

from readAtten import *
from writeAtten import writeAtten

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def readValues():

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

@app.route('/Atten1', methods = ['POST'])
def writeValue1():

    attenWrite = int(request.form.get('amountInput1'))
    writeAtten(1,attenWrite)

    return redirect('/')

@app.route('/Atten2', methods = ['POST'])
def writeValue2():

    attenWrite = int(request.form.get('amountInput2'))
    writeAtten(2,attenWrite)

    return redirect('/')

@app.route('/Atten3', methods = ['POST'])
def writeValue3():

    attenWrite = int(request.form.get('amountInput3'))
    writeAtten(3,attenWrite)

    return redirect('/')

@app.route('/Atten4', methods = ['POST'])
def writeValue4():

    attenWrite = int(request.form.get('amountInput4'))
    writeAtten(4,attenWrite)

    return redirect('/')

@app.route('/Atten5', methods = ['POST'])
def writeValue5():

    attenWrite = int(request.form.get('amountInput5'))
    writeAtten(5,attenWrite)

    return redirect('/')

@app.route('/Atten6', methods = ['POST'])
def writeValue6():

    attenWrite = int(request.form.get('amountInput6'))
    writeAtten(6,attenWrite)

    return redirect('/')

@app.route('/Atten7', methods = ['POST'])
def writeValue7():

    attenWrite = int(request.form.get('amountInput7'))
    writeAtten(7,attenWrite)

    return redirect('/')

@app.route('/Atten8', methods = ['POST'])
def writeValue8():

    attenWrite = int(request.form.get('amountInput8'))
    writeAtten(8,attenWrite)

    return redirect('/')

@app.route('/Atten9', methods = ['POST'])
def writeValue9():

    attenWrite = int(request.form.get('amountInput9'))
    writeAtten(9,attenWrite)

    return redirect('/')

@app.route('/Atten10', methods = ['POST'])
def writeValue10():

    attenWrite = int(request.form.get('amountInput10'))
    writeAtten(10,attenWrite)

    return redirect('/')

@app.route('/Atten11', methods = ['POST'])
def writeValue11():

    attenWrite = int(request.form.get('amountInput11'))
    writeAtten(11,attenWrite)

    return redirect('/')

@app.route('/Atten12', methods = ['POST'])
def writeValue12():

    attenWrite = int(request.form.get('amountInput12'))
    writeAtten(12,attenWrite)

    return redirect('/')

@app.route('/Atten13', methods = ['POST'])
def writeValue13():

    attenWrite = int(request.form.get('amountInput13'))
    writeAtten(13,attenWrite)

    return redirect('/')

@app.route('/Atten14', methods = ['POST'])
def writeValue14():

    attenWrite = int(request.form.get('amountInput14'))
    writeAtten(14,attenWrite)

    return redirect('/')

@app.route('/Atten15', methods = ['POST'])
def writeValue15():

    attenWrite = int(request.form.get('amountInput15'))
    writeAtten(15,attenWrite)

    return redirect('/')

@app.route('/Atten16', methods = ['POST'])
def writeValue16():

    attenWrite = int(request.form.get('amountInput16'))
    writeAtten(16,attenWrite)

    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=int("8080"))

