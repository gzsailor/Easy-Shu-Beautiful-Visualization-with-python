# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:24:48 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *

import matplotlib.pyplot as plt 

from datetime import datetime

df=pd.read_csv('Calendar.csv',parse_dates=['date'])

df['year']=[d.year for d in df['date']]

df=df[df['year']==2017]
df['month']=[d.month for d in df['date']]
month_label=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df['monthf']=df['month'].replace(np.arange(1,13,1), month_label)
df['monthf']=df['monthf'].astype("category",categories=month_label,ordered=True)


df['week']=[int(d.strftime('%W')) for d in df['date']]

df['weekay']=[int(d.strftime('%u')) for d in df['date']]

week_label=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
df['weekdayf']=df['weekay'].replace(np.arange(1,8,1), week_label)
df['weekdayf']=df['weekdayf'].astype("category",categories=week_label,ordered=True)


df['day']=[d.strftime('%d') for d in df['date']]


df['monthweek']=df.groupby('monthf')['week'].apply(lambda x: x-x.min()+1)


base_plot=(ggplot(df, aes('weekdayf', 'monthweek', fill='value')) + 
  geom_tile(colour = "white",size=0.1) + 
  scale_fill_cmap(name ='Spectral_r')+
  geom_text(aes(label='day'),size=8)+
  facet_wrap('~monthf' ,nrow=3) +
  scale_y_reverse()+
  xlab("Day") + ylab("Week of the month") +
  theme(strip_text = element_text(size=11,face="plain",color="black"),
        axis_title=element_text(size=10,face="plain",color="black"),
         axis_text = element_text(size=8,face="plain",color="black"),
         legend_position = 'right',
         legend_background = element_blank(),
         aspect_ratio =0.85,
        figure_size = (8, 8),
        dpi = 100
  ))
  
print(base_plot)






