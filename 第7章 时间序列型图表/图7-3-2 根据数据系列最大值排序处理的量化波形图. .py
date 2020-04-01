# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:35:21 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm,colors
from matplotlib.pyplot import figure, show, rc

#------------------------------------------(a)排序前----------------------------------------
df=pd.read_csv('StreamGraph_Data.csv',index_col =0)

labels=df.columns
cmap=cm.get_cmap('Paired',11)
color=[colors.rgb2hex(cmap(i)[:3]) for i in range(cmap.N) ] 

    
fig = figure(figsize=(5,4.5),dpi =90)     
plt.stackplot(df.index.values, df.values.T, labels=labels,baseline ='sym',colors=color,edgecolor='k',linewidth=0.25)
plt.legend(loc="center right",
          bbox_to_anchor=(1.2, 0, 0, 1),title='Group',edgecolor='none',facecolor='none') 
plt.show()
#fig.savefig('量化波形图1.pdf')
#=--------------------------------------(b)排序后.-------------------------------------------
df=pd.read_csv('StreamGraph_Data.csv',index_col =0)
df_colmax= (df.apply(lambda x: x.max(), axis=0)).sort_values(ascending=True)
N=len(df_colmax)
index=np.append(np.arange(0,N,2),np.arange(1,N,2)[::-1])
labels=df_colmax.index[index]

df=df[labels]

cmap=cm.get_cmap('Paired',11)
color=[colors.rgb2hex(cmap(i)[:3]) for i in range(cmap.N) ] 
    
fig = figure(figsize=(5,4.5),dpi =90)   
plt.stackplot(df.index.values, df.values.T, labels=labels,baseline ='wiggle',colors=color,edgecolor='k',linewidth=0.25)
plt.legend(loc="center right",
          bbox_to_anchor=(1.2, 0, 0, 1),title='Group',edgecolor='none',facecolor='none')
plt.show()
#fig.savefig('量化波形图2.pdf')