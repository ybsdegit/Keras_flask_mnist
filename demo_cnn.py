#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 15:44
# @Author  : Paulson
# @File    : demo.py
# @Software: PyCharm
# @define  : function

import tensorflow.keras as keras
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img


model_file = './model/model.h5'
model = keras.models.load_model(model_file)


file_name = 'output.png'

# 图片处理方式1
# img = Image.open(file_name).convert('L')
# img = img.resize((28,28))
# img.save('./99.png')
# img = np.reshape(img, (1, 28, 28, 1))
# img = img.astype('float32') / 255.

img = img_to_array(load_img('output.png', target_size=(28, 28), color_mode="grayscale")) / 255.

img = np.expand_dims(img, axis=0)
print(img.shape)
# img = img.reshape(1, 28, 28, 1)

predict = model.predict_classes(img)
print ('识别为：')
print (predict[0])