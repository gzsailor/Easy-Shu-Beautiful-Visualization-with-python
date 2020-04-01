# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:56:52 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
from plotnine import *
from datetime import datetime

df=pd.read_csv('StackedArea_Data.csv')

df['Date']=[datetime.strptime(d, '%Y/%m/%d').date() for d in df['Date']]
Sum_df=df.iloc[:,1:].apply(lambda x: x.sum(), axis=0).sort_values(ascending=True)
melt_df=pd.melt(df,id_vars=["Date"],var_name='variable',value_name='value')
melt_df['variable']=melt_df['variable'].astype("category",categories= Sum_df.index,ordered=True)

#----------------------------图6-1-4堆积面积图.(a) 堆积面积图--------------------------------
base_plot=(ggplot(melt_df, aes(x ='Date', y = 'value',fill='variable',group='variable') )+
  geom_area(position="stack",alpha=1)+ 
  geom_line(position="stack",size=0.25,color="black")+
  scale_x_date(date_labels = "%Y",date_breaks = "2 year")+
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
  xlab("Year")+ 
  ylab("Value")+
    theme(
        figure_size = (6, 5),
        dpi = 100))

print(base_plot)
#base_plot.save("堆积面积图.pdf")

#-----------------------------图6-1-4堆积面积图.  (b)百分比堆积面积图.----------------------------------

df=pd.read_csv('StackedArea_Data.csv')

df['Date']=[datetime.strptime(d, '%Y/%m/%d').date() for d in df['Date']]

SumRow_df=df.iloc[:,1:].apply(lambda x: x.sum(), axis=1)
df.iloc[:,1:]=df.iloc[:,1:].apply(lambda x: x/SumRow_df, axis=0)
meanCol_df=df.iloc[:,1:].apply(lambda x: x.mean(), axis=0).sort_values(ascending=True)
melt_df=pd.melt(df,id_vars=["Date"],var_name='variable',value_name='value')
melt_df['variable']=melt_df['variable'].astype("category",categories= meanCol_df.index,ordered=True)


base_plot=(ggplot(melt_df, aes(x ='Date', y = 'value',fill='variable',group='variable') )+
  geom_area(position="fill",alpha=1)+ 
  geom_line(position="fill",size=0.25,color="black")+
  scale_x_date(date_labels = "%Y",date_breaks = "2 year")+
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
  xlab("Year")+ 
  ylab("Value")+
  theme(
        figure_size = (6, 5),
        dpi = 100))

print(base_plot)
#base_plot.save("堆积面积图2.pdf")