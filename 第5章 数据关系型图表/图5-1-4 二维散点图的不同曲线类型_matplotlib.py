# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:43:16 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np
from plotnine import *
from skmisc.loess import loess #提供loess smoothing
df=pd.read_csv('Scatter_Data.csv')


#---------------------------图(f) loess数据平滑曲线-----------------------------
l = loess(df['x'], df['y'])
l.fit()
pred = l.predict(df['x'], stderror=True)
conf = pred.confidence()

y_fit = pred.values
ll = conf.lower
ul = conf.upper

fig=plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'],s=30,c='black')
plt.plot(df['x'], y_fit, color='r',linewidth=2,label='polyfit values')
plt.fill_between(df['x'],ll,ul, facecolor='r', edgecolor='none',interpolate=True,alpha=.33)
plt.show()

#-----------------------------图(b): 线性拟合曲线--------------------------------
fun = np.polyfit(df['x'], df['y'], 1)
poly= np.poly1d(fun)
print(poly)           #打印出拟合函数
y_fit =poly(df['x'])  #拟合y值


fig=plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'],s=30,c='black')
plt.plot(df['x'], y_fit, color='r',linewidth=2,label='polyfit values')



