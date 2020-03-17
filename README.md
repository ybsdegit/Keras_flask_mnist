# Keras_flask_mnist
基于 TensorFlow2.0 （Keras） + Flask 的 Mnist 手写数字集识别系统

### 更新记录
- 2020-03-17 使用redis实现记录访问次数的功能

### 部署
- 下载
```c
git clone https://github.com/ybsdegit/Keras_flask_mnist.git
```
- 安装依赖
```
pip install -r requirements.txt
```

# 运行

- 启动服务
```
python app.py
```
本地启动访问地址为：`http://localhost:3335/`

- 训练
源码中也包含训练好的模型 `model.h5`,测试集成功率99.9，也可以自行训练。
```
python model/train.py
```


### 博客
```
https://blog.csdn.net/qq_38534107/article/details/103565899
```


### 声明 （2019年12月16日晚23点）
识别率达到95%以上。已经是个成熟的demo了

求star
