# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:34:24 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *


df=pd.read_csv('Distribution_Data.csv')
df['class']=df['class'].astype("category",categories= ["n", "s", "k", "mm"],ordered=True)

#-------------------------------------------(a)抖动散点图-------------------------------------------
jitter_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_jitter(width=0.3,size=3,stroke=0.1,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(jitter_plot)
#jitter_plot.save("jitter_plot.pdf")  


#-------------------------------------------(b)蜂群图-------------------------------------------

sns.set_palette("husl") #设定绘图的颜色主题
fig = plt.figure(figsize=(4,4), dpi=100)
sns.swarmplot(x="class", y="value",hue="class", data=df,edgecolor='k',linewidth=0.2)
plt.legend().set_visible(False)

#-------------------------------------------(c)点阵图-------------------------------------------
dot_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_dotplot(binaxis = "y",stackdir ='center',
              binwidth=0.15,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(dot_plot)
#dot_plot.save("dot_plot.pdf") 


#-------------------------------------------(d) 带误差线的均值散点图-------------------------------------------
jitter_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_jitter(width=0.3,size=3,stroke=0.1,show_legend=False)
+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},geom="pointrange", color = "black",size = 1,show_legend=False)
#+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},geom="point", fill="w",color = "black",size = 5,stroke=1,show_legend=False)
+geom_point(stat="summary", fun_data="mean_sdl",fun_args = {'mult':1},fill="w",color = "black",size = 5,stroke=1,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(jitter_plot)
#jitter_plot.save("jitter_plot2.pdf")  

#-------------------------------------------(e) 带误差线散点与点阵组合图-------------------------------------------

dot_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_dotplot(binaxis = "y",stackdir ='center',
              binwidth=0.15,show_legend=False)
+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},geom="pointrange", color = "black",size = 1,show_legend=False)
+stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},geom="point", fill="w",color = "black",size = 5,stroke=1,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(dot_plot)
#dot_plot.save("dot_plot2.pdf")

#-------------------------------------------(f) 带连接线的带误差线散点图-------------------------------------------

df['time']=pd.factorize(df['class'])[0]
df_group=df.groupby(df['time'],as_index =False).agg({'value':{'mean': np.mean, 'std': np.std}})
df_group.columns = ['time','mean','std']

jitter_plot=(ggplot(df_group, aes(x ='time', y = 'mean', ymin = 'mean-std', ymax = 'mean+std'))
+geom_line(size=1,show_legend=False) 
+geom_errorbar(colour="black", width=0.2,size=1,show_legend=False)
+geom_point(aes(fill = 'factor(time)'),shape='o',size=6,stroke=0.75,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+ylab("value")
+xlim(-0.5,3.5)
+ylim(0,7)
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(jitter_plot)
jitter_plot.save("jitter_plot3.pdf")  