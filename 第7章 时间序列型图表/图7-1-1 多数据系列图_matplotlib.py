# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:00:19 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime

df=pd.read_csv('Line_Data.csv',index_col =0)

df.index=[datetime.strptime(d, '%Y/%m/%d').date() for d in df.index]

#---------------------------------------------图6-1-1 多数据系列图. (a)折线图--------------------
fig =plt.figure(figsize=(5,4), dpi=100)
plt.plot(df.index, df.AMZN, color='#F94306', label='AMZN')
plt.plot(df.index, df.AAPL, color='#06BCF9', label='AAPL')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left',edgecolor='none',facecolor='none')
plt.show()

#----------------------------------------图6-1-1 多数据系列图.(b)面积图.-------------------------
columns=df.columns
colors=["#F94306","#06BCF9"]
fig =plt.figure(figsize=(5,4), dpi=100)
plt.fill_between(df.index.values, y1=df.AMZN.values, y2=0, label=columns[1], alpha=0.75, facecolor=colors[0], linewidth=1,edgecolor ='k')
plt.fill_between(df.index.values, y1=df.AAPL.values, y2=0, label=columns[0], alpha=0.75, facecolor=colors[1], linewidth=1,edgecolor ='k')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left',edgecolor='none',facecolor='none')
plt.show()


#-------------------------------------图6-1-3 夹层填充面积图. (a)单色-----------------------------------------------------
df=pd.read_csv('Line_Data.csv')

df['date']=[datetime.strptime(d, '%Y/%m/%d').date() for d in df['date']]#df['date'].map(lambda x:datetime.datetime.strptime(x, '%Y/%m/%d').date())

df['ymin']=df[['AMZN','AAPL']].apply(lambda x: x.min(), axis=1)
df['ymax']=df[['AMZN','AAPL']].apply(lambda x: x.max(), axis=1)


fig =plt.figure(figsize=(5,4), dpi=100)
plt.fill_between(df.date.values, y1=df.ymax.values, y2=df.ymin.values, alpha=0.15, facecolor='black', linewidth=1,edgecolor ='k')
plt.plot(df.date, df.AMZN, color='#F94306', label='AMZN')
plt.plot(df.date, df.AAPL, color='#06BCF9', label='AAPL')
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left',edgecolor='none',facecolor='none')
plt.show()

