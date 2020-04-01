# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:58:09 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas.tools.plotting import parallel_coordinates,andrews_curves
from sklearn.preprocessing import scale

df=pd.read_csv('Parallel_Coordinates_Data.csv')

df['Class']=[ "Class1" if d>523 else "Class2" for d in df['reading']]

df.iloc[:,range(0,df.shape[1]-1)] = scale(df.iloc[:,range(0,df.shape[1]-1)] )

fig =plt.figure(figsize=(5.5,4.5), dpi=100)
parallel_coordinates(df,'Class',color=["#45BFFC","#90C539" ],linewidth=1)
                                       
plt.grid(b=0, which='both', axis='both')

plt.legend(loc="center right",
          bbox_to_anchor=(1.25, 0, 0, 1),edgecolor='none',facecolor='none',title='Group')  

ax = plt.gca()
ax.xaxis.set_ticks_position('top') 
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
plt.show()

