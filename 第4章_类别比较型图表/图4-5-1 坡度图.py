# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:31:44 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *

#------------------------------------(a)两年份对比--------------------------------------------
df=pd.read_csv('Slopecharts_Data1.csv')


left_label=df.apply(lambda x: x['Contry']+','+ str(x['1970']),axis=1)
right_label=df.apply(lambda x: x['Contry']+','+ str(x['1979']),axis=1)
df['class']=df.apply(lambda x: "red" if x['1979']-x['1970']<0 else "green",axis=1)

#list(map(lambda x,y:"red" if x-y<0 else "green", left_label,right_label))


base_plot=(ggplot(df) + 
  geom_segment(aes(x=1, xend=2, y='1970', yend='1979', color='class'), size=.75, show_legend=False) +  #连接线
  geom_vline(xintercept=1, linetype="solid", size=.1) + # 1952年的垂直直线
  geom_vline(xintercept=2, linetype="solid", size=.1) + # 1957年的垂直直线
  geom_point(aes(x=1, y='1970'), size=3,shape='o',fill="grey",color="black") + # 1952年的数据点
  geom_point(aes(x=2, y='1979'), size=3,shape='o',fill="grey",color="black") + # 1957年的数据点
  scale_color_manual(labels = ("Up", "Down"), values = ("#A6D854","#FC4E07")) +  
  xlim(.5, 2.5) )
# 添加文本信息
base_plot=( base_plot + geom_text(label=left_label, y=df['1970'], x=0.95,  size=10,ha='right')
+ geom_text(label=right_label, y=df['1979'], x=2.05, size=10,ha='left')
+ geom_text(label="1970", x=1, y=1.02*(np.max(np.max(df[['1970','1979']]))),  size=12)   
+ geom_text(label="1979", x=2, y=1.02*(np.max(np.max(df[['1970','1979']]))),  size=12) 
+theme_void()
+  theme(
    aspect_ratio =1.5,
    figure_size = (5, 6),
     dpi = 100
  )
)
print(base_plot)

#------------------------------------------(b)多年份对比---------------------------------------------------

df=pd.read_csv('Slopecharts_Data2.csv')

df['group']=df.apply(lambda x: "green" if x['2007']>x['2013'] else "red",axis=1)

df2=pd.melt(df, id_vars=["continent",'group'])

df2.value=df2.value.astype(int)
df2.variable=df2.variable.astype(int)

left_label =df2.apply(lambda x:  x['continent']+','+ str(x['value']) if x['variable']==2007 else "",axis=1)
right_label=df2.apply(lambda x:  x['continent']+','+ str(x['value']) if x['variable']==2013 else "",axis=1)

left_point=df2.apply(lambda x: x['value'] if x['variable']==2007 else np.nan,axis=1)
right_point=df2.apply(lambda x: x['value'] if x['variable']==2013 else np.nan,axis=1)



base_plot=( ggplot(df2) + 
  geom_line(aes(x='variable', y='value',group='continent', color='group'),size=.75) + 
  geom_vline(xintercept=2007, linetype="solid", size=.1) + 
  geom_vline(xintercept=2013, linetype="solid", size=.1) +
  geom_point(aes(x='variable', y=left_point), size=3,shape='o',fill="grey",color="black") + 
  geom_point(aes(x='variable', y=right_point), size=3,shape='o',fill="grey",color="black") + 
  scale_color_manual(labels = ("Up", "Down"), values = ("#FC4E07",  "#A6D854")) +  
  xlim(2001, 2018) )

base_plot=( base_plot + geom_text(label=left_label, y=df2['value'], x=2007,  size=9,ha='right')
+ geom_text(label=right_label, y=df2['value'], x=2013, size=9,ha='left')
+ geom_text(label="2007", x=2007, y=1.05*(np.max(df2.value)),  size=12)   
+ geom_text(label="2013", x=2013, y=1.05*(np.max(df2.value)),  size=12) 
+theme_void()
+  theme(
    aspect_ratio =1.2,
    figure_size = (7, 9),
     dpi = 100
  )
)

print(base_plot)