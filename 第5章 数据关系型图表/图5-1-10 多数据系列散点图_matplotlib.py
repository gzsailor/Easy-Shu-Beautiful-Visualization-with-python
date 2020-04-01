# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:51:28 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd
df=pd.read_csv('MultiSeries_Scatter_Data.csv')
group=np.unique(df.label_pred)
markers=['o','s']  
colors=["#00AFBB",  "#FC4E07"]
fig =plt.figure(figsize=(4,4), dpi=100)
for i in range(0,len(group)):
    temp_df=df[df.label_pred==group[i]]
    plt.scatter(temp_df.x, temp_df.y,
                s=40, linewidths=0.5, edgecolors="k",alpha=0.8,
                marker=markers[i], c=colors[i],label=group[i])
plt.xlim(-5,10)
plt.ylim(-5,10)
plt.legend(title='group',loc='lower right',edgecolor='none',facecolor='none')
plt.show()
