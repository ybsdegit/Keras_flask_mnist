#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:27
# @Author  : Paulson
# @File    : app.py
# @Software: PyCharm
# @define  : function
import os
import re
import sys
import base64
import numpy as np
from flask import Flask, render_template,request
from scipy.misc import imsave, imread, imresize
import tensorflow.keras.models

sys.path.append(os.path.abspath("./model"))
from model.load import *
app = Flask(__name__, template_folder='template')
global model, graph
model, graph = init()

def convertImage(imgData1):
    imgstr = re.search(b'data:image/png;base64,(.*)', imgData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    x = imread('output.png',mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))
    x = x.reshape(1,28,28,1)
    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out,axis=1))
        response = np.array_str(np.argmax(out,axis=1))
        return response

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    app.run()