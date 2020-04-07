#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 14:27
# @Author  : Paulson
# @File    : app.py
# @Software: PyCharm
# @define  : function

import re
import json
import base64
import numpy as np
import tensorflow.keras as keras
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# 使用 redis 统计总访问次数，今日访问次数
from redis_util import get_today, get_visit_num_all, get_visit_num_today, inc_visit_num

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

model_file = './model/model.h5'
global model
model = keras.models.load_model(model_file)

@app.route('/')
def home():
    inc_visit_num()
    response = get_visit_info()
    return jsonify(response)  # 如果没有使用 redis 统计访问次数功能，请使用index.html

@app.route('/home')
def index():
    inc_visit_num()
    response = get_visit_info()
    return jsonify(response)  # 如果没有使用 redis 统计访问次数功能，请使用index.html

@app.route('/predict/', methods=['Get', 'POST'])
def preditc():
    inc_visit_num()  # 每访问一次，增加访问次数
    parseImage(request.get_data())
    img = img_to_array(load_img('output.png', target_size=(28, 28), color_mode="grayscale")) / 255.
    img = np.expand_dims(img, axis=0)
    code = model.predict_classes(img)[0]
    response = get_visit_info(int(code))
    print(response)
    return jsonify(response)

def get_visit_info(code=0):
    response = {}
    response['code'] = code
    response['visits_all'] = get_visit_num_all()
    response['visits_today'] = get_visit_num_today()
    response['today'] = get_today()
    return response

def parseImage(imgData):
    imgStr = re.search(b'base64,(.*)', imgData).group(1)
    with open('./output.png', 'wb') as output:
        output.write(base64.decodebytes(imgStr))
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3335)