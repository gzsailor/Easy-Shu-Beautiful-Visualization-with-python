# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:11:15 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime

#-----------------------------------(a) 堆积面积图--------------------------------------------
#from matplotlib.ticker import FormatDateFormatter
df=pd.read_csv('StackedArea_Data.csv',index_col =0)
df.index=[datetime.strptime(d, '%Y/%m/%d').date() for d in df.index]

Sum_df=df.apply(lambda x: x.sum(), axis=0).sort_values(ascending=False)

df=df[Sum_df.index]

columns=df.columns

colors= sns.husl_palette(len(columns),h=15/360, l=.65, s=1).as_hex() 

fig =plt.figure(figsize=(5,4), dpi=100)
plt.stackplot(df.index.values, 
              df.values.T,alpha=1, labels=columns, linewidth=1,edgecolor ='k',colors=colors)

plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(title="group",loc="center right",bbox_to_anchor=(1.5, 0, 0, 1),edgecolor='none',facecolor='none')
#plt.gca().xaxis.set_major_formatter(FormatDateFormatter('%Y'))
#ax=plt.gca()
#ax.xaxis.set_major_locator(mdates.MonthLocator(interval=24))
plt.show()

#---------------------------------(b)百分比堆积面积图---------------------------------------------
df=pd.read_csv('StackedArea_Data.csv',index_col =0)
df.index=[datetime.strptime(d, '%Y/%m/%d').date() for d in df.index]
SumRow_df=df.apply(lambda x: x.sum(), axis=1)
df=df.apply(lambda x: x/SumRow_df, axis=0)
meanCol_df=df.apply(lambda x: x.mean(), axis=0).sort_values(ascending=False)
df=df[meanCol_df.index]
columns=df.columns

colors= sns.husl_palette(len(columns),h=15/360, l=.65, s=1).as_hex() 

fig =plt.figure(figsize=(5,4), dpi=100)
plt.stackplot(df.index.values, df.values.T,labels=columns,colors=colors,
              linewidth=1,edgecolor ='k')

plt.xlabel("Year")
plt.ylabel("Value")
plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()]) 
plt.legend(title="group",loc="center right",bbox_to_anchor=(1.5, 0, 0, 1),edgecolor='none',facecolor='none')

plt.show()