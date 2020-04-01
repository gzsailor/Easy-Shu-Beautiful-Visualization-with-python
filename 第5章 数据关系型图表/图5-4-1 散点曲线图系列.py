# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:01:25 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from plotnine import *
from scipy import interpolate

df=pd.read_csv('Line_Data.csv')

#-----------------------------------------(a)-------------------------------------------
Line_plot1=(ggplot(df, aes('x', 'y') )+
  geom_line( size=0.25)+
  geom_point(shape='o',size=4,color="black",fill="#F78179") +
  xlab("X-Axis")+
  ylab("Y-Axis")+
  ylim(0, 50)+
  theme(
       axis_title=element_text(size=15,face="plain",color="black"),
        axis_text = element_text(size=13,face="plain",color="black"),
      legend_position="none",
      aspect_ratio =1.1,
       figure_size = (4, 4),
       dpi = 100
       )
  )
print(Line_plot1)

#-----------------------------------------(b)-------------------------------------------
Line_plot2=(ggplot(df, aes('x', 'y') )+
  geom_line( size=1)+
  #geom_point(shape='o',size=4,color="black",fill="#F78179") +
  xlab("X-Axis")+
  ylab("Y-Axis")+
  ylim(0, 50)+
  theme_gray()+
  theme(
       axis_title=element_text(size=15,face="plain",color="black"),
        axis_text = element_text(size=13,face="plain",color="black"),
      legend_position="none",
      aspect_ratio =1.1,
       figure_size = (4, 4),
       dpi = 100
       )
  )
print(Line_plot2)

#-----------------------------------------(c)-------------------------------------------

Line_plot3=(ggplot(df, aes('x', 'y') )+
  geom_line( size=1)+
  geom_area(fill="#F78179",alpha=0.7)+
  geom_point(shape='o',size=4,color="black",fill="w") +
  xlab("X-Axis")+
  ylab("Y-Axis")+
  ylim(0, 50)+
  theme_gray()+
  theme(
       axis_title=element_text(size=15,face="plain",color="black"),
        axis_text = element_text(size=13,face="plain",color="black"),
      legend_position="none",
      aspect_ratio =1.1,
       figure_size = (4, 4),
       dpi = 100
       )
  )
print(Line_plot3)


#-----------------------------------------(d)-------------------------------------------

f = interpolate.interp1d(df['x'], df['y'])#, kind='slinear')#kind='linear', 

x_new=np.linspace(np.min(df['x']),np.max(df['x']),100)
y_new=f(x_new)
df_interpolate = pd.DataFrame({'x': x_new,'y':y_new})

Line_plot2=(ggplot()+
  geom_area(df_interpolate, aes('x', 'y'),size=1,fill="#F78179",alpha=0.7)+
  geom_line(df_interpolate, aes('x', 'y'),size=1)+
  geom_point(df, aes('x', 'y'),shape='o',size=4,color="black",fill="white") +
  xlab("X-Axis")+
  ylab("Y-Axis")+
  ylim(0, 50)+
  theme_gray()+
  theme(
       axis_title=element_text(size=15,face="plain",color="black"),
        axis_text = element_text(size=13,face="plain",color="black"),
      legend_position="none",
      aspect_ratio =1.1,
       figure_size = (4, 4),
       dpi = 100
       )
  )
print(Line_plot2)
