#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:27
# @Author  : Paulson
# @File    : app.py
# @Software: PyCharm
# @define  : function

from flask import Flask, render_template, request
import numpy as np
import tensorflow.keras as keras
import re
import base64
from tensorflow.keras.preprocessing.image import img_to_array, load_img

app = Flask(__name__)

model_file = './model/model.h5'
global model
model = keras.models.load_model(model_file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['Get', 'POST'])
def preditc():
    parseImage(request.get_data())
    img = img_to_array(load_img('output.png', target_size=(28, 28), color_mode="grayscale")) / 255.
    img = np.expand_dims(img, axis=0)
    response = model.predict_classes(img)[0]
    return str(response)

def parseImage(imgData):
    imgStr = re.search(b'base64,(.*)', imgData).group(1)
    with open('./output.png', 'wb') as output:
        output.write(base64.decodebytes(imgStr))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3335)