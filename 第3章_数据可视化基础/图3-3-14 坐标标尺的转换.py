# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:15:23 2019

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

df=pd.read_csv("logarithmic_scale.csv")
df_melt=pd.melt(df,id_vars='VIN(V)',var_name='Class',value_name='value')

p1=(ggplot(df_melt,aes(x='VIN(V)',y='value',color='Class')) + 
  geom_line(size=1)+
  scale_x_continuous(breaks=np.arange(-20,21,5),limits=(-20,20)) +
  scale_y_continuous(breaks=np.arange(0,2.1,0.5),limits=(0,2))+
   scale_color_manual(values=("#36BED9","#FF0000"))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        panel_grid_major=element_line(color="#C7C7C7",linetype ='--'),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5),
     legend_position=(0.8,0.8),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("logarithmic_scale1.pdf") 


p1=(ggplot(df_melt,aes(x='VIN(V)',y='value',color='Class')) + 
  geom_line(size=1)+
  scale_x_continuous(breaks=np.arange(-20,21,5),limits=(-20,20)) +
  scale_y_log10(name='log(value)',limits=(0.00001,10))+
   scale_color_manual(values=("#36BED9","#FF0000"))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        panel_grid_major=element_line(color="#C7C7C7",linetype ='--'),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5),
     legend_position=(0.8,0.8),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("logarithmic_scale2.pdf") 