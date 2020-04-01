# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:14:54 2019

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

df=pd.read_csv("MappingAnalysis_Data.csv")


p1=(ggplot(df,aes(x='Time',y='value',group='variable')) + 
  geom_line()+
  geom_point(shape='o',size=4,colour="black",fill="white") +
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("plotnine9.pdf") 


p2=(ggplot(df,aes(x='Time',y='value',fill='variable')) + 
  geom_line()+
  geom_point(shape='o',size=4,colour="black") +
  scale_fill_manual(values=("#595959","#BFBFBF","black","white"))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p2)
#p2.save("plotnine9.1.pdf") 


p3=(ggplot(df,aes(x='Time',y='value',shape='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black",fill="#BFBFBF") +
   scale_shape_manual(values=('o','s','D','^'))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p3)
#p3.save("plotnine10.pdf") 

p4=(ggplot(df,aes(x='Time',y='value',fill='variable')) + 
  geom_line()+
  geom_point(shape='o',size=4,colour="black") +
   scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D"))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p4)
#p4.save("plotnine11.pdf")


p5=(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black") +
  scale_fill_manual(values=("#595959","#BFBFBF","black","white"))+
  scale_shape_manual(values=('o','s','D','^'))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p5)
#p5.save("plotnine12.pdf") 


p6=(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black") +
  scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D"))+
  scale_shape_manual(values=('o','s','D','^'))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(4,4),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p6)
#p6.save("plotnine13.pdf") 



#-------------------------------------------------------------------------------
p6=(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black") +
  scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D"))+
  #scale_shape_manual(values=('o','s','D','^'))+
 # scale_x_continuous(name="Time(d)",breaks=np.arange(0,21,2),limits=(0,20))+        
  scale_y_continuous(breaks=np.arange(0,91,10),limits=(0,90),expand =(0, 1))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5),
     legend_position=(0.32,0.75),
     legend_background=element_rect(fill="none"))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p6)
#p6.save("plotnine13_1.pdf") 


p6=(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black") +
  scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D"))+
  scale_shape_manual(values=('o','s','D','^'))+
  scale_x_continuous(name="Time(d)",breaks=np.arange(0,21,2),limits=(0,20))+        
  scale_y_continuous(breaks=np.arange(0,91,10),limits=(0,90),expand =(0, 1))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p6)
#p6.save("plotnine14.pdf") 

p6=(ggplot(df,aes(x='Time',y='value',shape='variable',fill='variable')) + 
  geom_line()+
  geom_point(size=4,colour="black") +
  scale_fill_manual(values=("#FF9641","#FF5B4E","#B887C3","#38C25D"))+
  scale_shape_manual(values=('o','s','D','^'))+
  scale_x_continuous(name="Time(d)",breaks=np.arange(0,21,2),limits=(0,20))+        
  scale_y_continuous(breaks=np.arange(0,91,10),limits=(0,90),expand =(0, 1))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5),
     legend_position=(0.32,0.75),
     legend_background=element_blank())) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p6)
#p6.save("plotnine15.pdf") 