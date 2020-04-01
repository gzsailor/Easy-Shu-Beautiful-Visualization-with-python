# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:53 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from plotnine import *
import pandas as pd
import numpy as np
from skmisc.loess import loess as loess_klass

filename='Facet_Data.csv'
file = open(filename, errors='ignore')#encoding="utf_8_sig'",
df=pd.read_csv(file)
df.head()
df.info()

#--------------------------- (a) 列分面的散点图 -----------------------------------------------------

base_plot=(ggplot(df, aes(x = 'tau', y = 'SOD', fill = 'Class')) +
  geom_point(size=3,shape='o',colour="black",show_legend=False) +
  #stat_smooth(method = 'loess',show_legend=False)+
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
  facet_wrap('~ Class'))
print(base_plot)

#--------------------------- (b) 列分面的带拟合曲线的散点图-----------------------------------------------------
base_plot=(ggplot(df, aes(x = 'tau', y = 'SOD',fill = 'Class')) +
  geom_point(size=2,shape='o',fill = 'black',colour="black",alpha=0.5,show_legend=False) +
  stat_smooth(method = 'loess',show_legend=False,alpha=0.7)+
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
  facet_wrap('~ Class'))
print(base_plot)


#-------------------------(a) 列分面的气泡图 ----------------------------------------------------
base_plot=(ggplot(df, aes(x = 'tau', y = 'SOD', fill= 'Class', size = 'age')) +
#其气泡的颜色填充由Class映射，大小由age映射
  geom_point(shape='o',colour="black",alpha=0.7) +
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
 #设置气泡类型为空心的圆圈，边框颜色为黑色，填充颜色透明度为0.7
  facet_wrap( '~ Class'))  #类别Class为列变量
print(base_plot)

#---------------------------------- (b) 列分面的带颜色映射的气泡图-----------------------------------------------------

base_plot=(ggplot(df, aes(x = 'tau', y = 'SOD', fill='age', size = 'age')) +
  geom_point(shape='o',colour="black",alpha=0.95) +
  scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = df['age'].mean())+
  facet_wrap( '~ Class'))
print(base_plot)

#------------------------------图9-2-4 矩阵分面气泡图-----------------------------------------------
df['gender']=df['gender'].astype('category')
df['gender'].cat.categories=['Female','Male']
base_plot=(ggplot(df, aes(x = 'tau', y = 'SOD', fill= 'Class', size = 'age')) + 
#其气泡的颜色填充由Class映射，大小由age映射
  geom_point(shape='o',colour="black",alpha=0.7) + 
  scale_fill_manual(values=("#FF0000","#00A08A","#F2AD00"))+
  #scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
#设置气泡类型为空心的圆圈，边框颜色为黑色，填充颜色透明度为0.7
  facet_grid('gender ~ Class') )# 性别Gender为行变量、类别Class为列变量
print(base_plot)