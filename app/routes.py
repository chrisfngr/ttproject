from app import app
from flask import Flask,render_template,request

import random

def randomRole():
    random.randint(1,2)

test = {'nameI':None,'role':None}

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/name')
def getName():
    return render_template('signin.html')

@app.route('/InputName', methods = ['GET','POST'])
def inputN():
    if request.method == 'POST':
        name = request.form['iname']
        test['nameI'] = name
        test['role'] = 'reciver'

        return render_template('matchP.html', name = test['nameI'],role = test['role'])

    return render_template('home.html')

@app.route('/guess', methods = ['GET','POST'] )
def getMatch():
    if request.method == 'POST':
        optionTrue = request.form.get('optionsRadios')
        if test['role'] == 'sender':
            optionCheap = request.form.get('optionsRadiosCheap')
        else:
            optionNumber = request.form.get('optionsRadiosNumber')
        print(optionTrue)
        #print(optionCheap)
        print(optionNumber)
        return render_template('shitou.html')

    return render_template('home.html')
