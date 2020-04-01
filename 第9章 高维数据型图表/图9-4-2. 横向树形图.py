# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:12:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import scipy.cluster.hierarchy as shc
import numpy as np
from matplotlib import cm,colors
from matplotlib import pyplot as plt
import pandas as pd
from plotnine.data import mtcars
from sklearn.preprocessing import scale
plt.rcParams['axes.facecolor']='w'
plt.rc('axes',axisbelow=True)  


df=mtcars.set_index('name')
df.loc[:,:] = scale(df.values )

#-------------------------------------------横向树形图-----------------------------------------------

fig=plt.figure(figsize=(10, 10), dpi= 80)
dend = shc.dendrogram(shc.linkage(df,method='ward'), orientation='left',
                      labels=df.index.values, color_threshold=5
                      )
plt.xticks(fontsize=13,rotation=0)
plt.yticks(fontsize=14)
#plt.grid(color='gray',which='major', axis='x',linestyle='--')

ax = plt.gca()
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('k')
ax.spines['bottom'].set_color('k')

#plt.savefig('树状图1.pdf')
plt.show()

#-------------------------------------------纵向树形图-----------------------------------------------
fig=plt.figure(figsize=(5, 5), dpi= 80)
#plt.title("USArrests Dendograms", fontsize=22)
dend = shc.dendrogram(shc.linkage(df.values.T,method='ward'), orientation='top',
                      labels=df.columns.values, color_threshold=5,
                      )
plt.xticks(fontsize=13,rotation=0)
plt.yticks(fontsize=14)
#plt.grid(color='gray',which='major', axis='y',linestyle='--')

ax = plt.gca()
ax.spines['left'].set_color('k')
ax.spines['right'].set_color('k')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')

#plt.savefig('树状图2.pdf')
plt.show()
