# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:26 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from pandas.plotting import radviz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv('iris.csv')

angle=np.arange(360)/180*3.14159
x=np.cos(angle)
y=np.sin(angle)

fig =plt.figure(figsize=(3.5,3.5), dpi=100)
ax=radviz(df, 'variety',color=['#FC0000','#F0AC02','#009E88'],
            edgecolors='k',marker='o',s=34,linewidths=1)
plt.plot(x,y,color='gray')
plt.axis('off')
plt.legend(loc="center",bbox_to_anchor=(1.1, 0, 0, 0.4),edgecolor='none',facecolor='none',title='Group')  