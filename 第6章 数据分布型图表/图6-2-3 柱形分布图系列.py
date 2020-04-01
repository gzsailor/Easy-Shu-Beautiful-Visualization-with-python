# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:39:25 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

df=pd.read_csv('Distribution_Data.csv')
df['class']=df['class'].astype("category",categories= ["n", "s", "k", "mm"],ordered=True)


#-------------------------------------------(a)带误差线的柱形图-------------------------------------------
Barjitter_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+stat_summary(fun_data="mean_sdl",fun_args = {'mult':1}, 
              geom="bar", color = "black",size = 0.75,width=0.7,show_legend=False)
+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},
              geom="errorbar", color = "black",size = 0.75,width=.2,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+ylim(0,7)
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(Barjitter_plot)
#Barjitter_plot.save("Barjitter_plot.pdf") 

#-------------------------------------------(b)带误差线柱形与抖动图-------------------------------------------

Barjitter_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},
              geom="bar", fill="w",color = "black",size =0.75,width=0.7,show_legend=False)
+stat_summary(fun_data="mean_sdl",fun_args = {'mult':1}, 
              geom="errorbar", color = "black",size = 0.75,width=.2,show_legend=False)
+geom_jitter(width=0.3,size=2,stroke=0.1,shape='o',show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+ylim(0,7)
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(Barjitter_plot)
#Barjitter_plot.save("Barjitter_plot2.pdf") 