# CNN: cats vs dogs classification

## 流程图

![流程图](./%E6%B5%81%E7%A8%8B%E5%9B%BE.jpg)

## 算法思路

### 准备数据

读取数据文件，制作训练标签  

```python
train_df = pd.DataFrame({
    'id': train_filenames,
    'label': train_labels
})
```

使用train_test_split划分训练集、验证集  

为了提高训练效果，使用*preprocessing.image.ImageDataGenerator*来增强数据集，利用多种能够生成可信图像的随机变换来增加样本，验证机不需要数据增强  

### 搭建模型

可视乎模型结构：

![plot_model](./%E5%8F%AF%E8%A7%86%E5%8C%96/plot_model.png)





同时定义训练时用的优化器、损失函数和准确率评测标准和提前结束训练方法  



### 训练并保存模型

```python
history = model.fit(train_generator,
    validation_data=valid_generator,
    steps_per_epoch=round(TRAIN_SIZE*(1.-VALID_FRACTION)/BATCH_SIZE),
    validation_steps=round(TRAIN_SIZE*VALID_FRACTION/BATCH_SIZE),
    epochs=EPOCHS,
    callbacks=[es],
    verbose=1)

```

训练在第30轮时提前终止，保存模型为model.h5  



### 可视化训练过程

Training accuracy & Validation accuracy:  

![Training accuracy & Validation accuracy](./%E5%8F%AF%E8%A7%86%E5%8C%96/Training%20accuracy%20%26%20Validation%20accuracy.jpg)

 

Training loss & Validation loss:  

![Training loss & Validation loss](./%E5%8F%AF%E8%A7%86%E5%8C%96/Training%20loss%20%26%20Validation%20loss.jpg)



### 预测

准备预测数据后进行预测，sigmoid返回0到1之间的概率，需要将其转换为一个整数类  

```python
yhat = [1 if y > 0.5 else 0 for y in yhat]
```

转化标签  

{ 'dog': 1, 'cat': 0 }



### 可视乎图像的预测结果

选取15个图片样本，输出图片和其对应的预测结果  

![Vis](./%E5%8F%AF%E8%A7%86%E5%8C%96/Sample%20Predicted%20Result.jpg)



### 加载保存模型，预测单张图像

```python
loaded_model = tf.keras.models.load_model('./model.h5')
```

选择10032.jpg  

![single](./%E5%8F%AF%E8%A7%86%E5%8C%96/Single%20sample%20prediction.jpg)

预测正确✅



### Qt界面实现

使用PyQt5实现了一个简单界面，可以选择图片在展示区显示，预测区显示预测的分类  
![1](./%E7%95%8C%E9%9D%A2%E5%AE%9E%E7%8E%B01.jpg)
![2](./%E7%95%8C%E9%9D%A2%E5%AE%9E%E7%8E%B02.jpg)
![3](./%E7%95%8C%E9%9D%A2%E5%AE%9E%E7%8E%B03.jpg)

