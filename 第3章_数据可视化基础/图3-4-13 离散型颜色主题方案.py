# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:46:22 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
#from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib
#plt.rc('font',family='Times New Roman')
matplotlib.rcParams['font.family'] = 'Times New Roman'

df=pd.read_csv("Facet_Data.csv")

p2=(ggplot(df, aes(x='SOD',y='tau',fill='Class'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_discrete()
  +theme(text=element_text(size=12,colour = "black"),
         legend_background=element_blank(),
         legend_position=(0.75,0.25),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
#p2.save('颜色主题方案1.pdf')


p1=(ggplot(df, aes(x='SOD',y='tau',fill='Class'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_brewer(type='qualitative', palette='Set1')
  +theme(text=element_text(size=12,colour = "black"),
           legend_background=element_blank(),
         legend_position=(0.75,0.25),
      aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save('颜色主题方案2.pdf')

p2=(ggplot(df, aes(x='SOD',y='tau',fill='Class'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_hue(s = 1, l = 0.65, h=0.0417,color_space='husl')
  +theme(text=element_text(size=12,colour = "black"),
           legend_background=element_blank(),
         legend_position=(0.75,0.25),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
#p2.save('颜色主题方案3.pdf')


p2=(ggplot(df, aes(x='SOD',y='tau',fill='Class'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_manual(values=("#E7298A","#66A61E","#E6AB02"))
  +theme(text=element_text(size=12,colour = "black"),
           legend_background=element_blank(),
         legend_position=(0.75,0.25),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
#p2.save('颜色主题方案4.pdf')
