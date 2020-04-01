# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:51:20 2019

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

#-----------------------------------(a) age映射到点的大小size--------------------------
p1=(ggplot(df, aes(x='SOD',y='tau',size='age')) + 
  geom_point(shape='o',color="black",
             fill="#336A97",stroke=0.25,alpha=0.8)+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("plotnine1.pdf") 


#----------------------------------(b) age映射到点的大小size和填充颜色fill------------------
p2=(ggplot(df, aes(x='SOD',y='tau',size='age',fill='age')) + 
  geom_point(shape='o',color="black",stroke=0.25, alpha=0.8)+
  #scale_fill_distiller(type='seq', palette='blues') +
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
#p2.save("plotnine2.pdf") 

#-------------------------(c) Class映射到点的颜色填充fill----------------------------------
p3=(ggplot(df, aes(x='SOD',y='tau',fill='Class')) + 
  geom_point(shape='o',size=3,colour="black",stroke=0.25)+
  #scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p3)
#p3.save("plotnine3.pdf") 

#-------------------------(d) age和Class分别映射到点的大小size和颜色fill--------------------
p4=(ggplot(df, aes(x='SOD',y='tau',size='age',fill='Class')) + 
  geom_point(shape='o',colour="black",stroke=0.25, alpha=0.8)+
  #scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p4)
p4.save("plotnine4.pdf") 
