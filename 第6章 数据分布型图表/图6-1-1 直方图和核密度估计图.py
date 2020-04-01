# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:54:07 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


import pandas as pd
#import numpy as np
#import seaborn as sns
from plotnine import *

#file = open('Hist_Density_Data.csv') #encoding='utf-8', 
df=pd.read_csv('Hist_Density_Data.csv')
#file.close()  # 关闭文件

#--------------------------------------------(a2) 多数剧系列直方图-----------------------------------

base_hist=(ggplot(df, aes(x='MXSPD', fill='Location'))+  
  geom_histogram(binwidth = 1,alpha=0.55,colour="black",size=0.25)+#, aes(fill = ..count..) )
  scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
  theme(
    text=element_text(size=13,color="black"),
    plot_title=element_text(size=15,family="myfont",face="bold.italic",hjust=.5,color="black"),#,
    legend_position=(0.7,0.8),
    legend_background = element_blank(),
    aspect_ratio =1.15,
    figure_size=(5,5)
  ))
print(base_hist)
#----------------------------------------(b2)多数剧系列核密度估计图----------------------------------
base_density=(ggplot(df, aes(x='MXSPD',  fill='Location'))+ 
  geom_density(bw=1,alpha=0.55,colour="black",size=0.25,kernel="gaussian")+
  scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
  theme(
    text=element_text(size=13,color="black"),
    plot_title=element_text(size=15,family="myfont",face="bold.italic",hjust=.5,color="black"),#,
    legend_position=(0.7,0.75),
    legend_background = element_blank(),
    aspect_ratio =1.15,
    figure_size=(5,5)
  ))
print(base_density)