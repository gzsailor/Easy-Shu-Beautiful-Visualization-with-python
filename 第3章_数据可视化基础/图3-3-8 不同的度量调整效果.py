# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:15:09 2019

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


#-------------------------------(a) 点大小size的度量调整 ------------------------
p5=(ggplot(df, aes(x='SOD',y='tau',size='age')) + 
  geom_point(shape='o',color="black",
             fill="#FF0000",stroke=0.25,alpha=0.8)+
             scale_size(range = (1, 8))+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p5)
#p5.save("plotnine5.pdf") 

#---------------------------(b) 点大小size和填充颜色fill的度量调整----------------
p6=(ggplot(df, aes(x='SOD',y='tau',fill='age',size='age')) + 
  geom_point(shape='o',color="black",stroke=0.25,alpha=0.8)+
             scale_size(range = (1, 8))+
             scale_fill_distiller(type='seq', palette='reds') +
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p6)
#p6.save("plotnine6.pdf") 


#-------------------------------(c)点颜色填充fill与形状shape的度量调整-------------------
p7=(ggplot(df, aes(x='SOD',y='tau',fill='Class',shape='Class')) + 
  geom_point(size=3,colour="black",stroke=0.25)+
  scale_fill_manual(values=("#36BED9","#FF0000","#FBAD01"))+
   scale_shape_manual(values=('o','s','D'))+
   #scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p7)
p7.save("plotnine7.pdf") 

#-------------------------------(d)点大小size和颜色fill的度量调整-----------------
p8=(ggplot(df, aes(x='SOD',y='tau',size='age',fill='Class')) + 
  geom_point(shape='o',colour="black",stroke=0.25, alpha=0.8)+
  scale_fill_manual(values=("#36BED9","#FF0000","#FBAD01"))+
  scale_size(range = (1, 8))+
             theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p8)
#p8.save("plotnine8.pdf") 
