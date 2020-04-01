# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:22:53 2020

@author: Soham Ghosh
"""
from flask import Flask, render_template,request
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    return render_template('test.html')

@app.route('/predict',method="POST")
def predict():
    print(request.form)
    features=[int(x) for x in request.form.values()]
    final=[np.array(features)]
    print(features)
    print(final)
    prediction=model.predictproba(final)
    output='{0:.{1}f}'.format(prediction[0][1],2)
    
    return render_template('test.html',pred='ANALYSIS IS {}'.format(output))

if __name__=='__main__':
    app.run(debug=True, host='192.168.0.5') #, host='192.168.0.5', port='6000')
