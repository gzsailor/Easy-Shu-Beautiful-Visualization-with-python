# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:28:20 2019

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


#---------------------------------------------------------------------------------
p2=(ggplot(df, aes(x='SOD',y='tau',fill='age'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_distiller(type='div',palette="RdYlBu")
  +guides(fill=guide_colorbar(barheight =80,barwidth=20))
  +theme(text=element_text(size=12,colour = "black"),
         legend_background=element_blank(),
         legend_position=(0.75,0.3),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
p2.save('颜色主题方案5.pdf')

p1=(ggplot(df, aes(x='SOD',y='tau',fill='age'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_cmap(name='viridis')
  +guides(fill=guide_colorbar(barheight =80,barwidth=20))
  +theme(text=element_text(size=12,colour = "black"),
         legend_background=element_blank(),
         legend_position=(0.75,0.3),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
p1.save('颜色主题方案6.pdf')

p2=(ggplot(df, aes(x='SOD',y='tau',fill='age'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = np.mean(df.age))
  +guides(fill=guide_colorbar(barheight =80,barwidth=20))
  +theme(text=element_text(size=12,colour = "black"),
         legend_background=element_blank(),
         legend_position=(0.75,0.3),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
p2.save('颜色主题方案7.pdf')

p2=(ggplot(df, aes(x='SOD',y='tau',fill='age'))  
  +geom_point(shape='o',color="black",size=3,
             stroke=0.25,alpha=1)
  +scale_fill_gradientn(colors= ("#82C143","white","#CB1B81"))
  +guides(fill=guide_colorbar(barheight =80,barwidth=20))
  +theme(text=element_text(size=12,colour = "black"),
         legend_background=element_blank(),
         legend_position=(0.75,0.3),
        aspect_ratio =1.15,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
p2.save('颜色主题方案8.pdf')

