# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:34:05 2019

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

N=20
df1 =pd.DataFrame(dict(x=np.sort(np.random.randn(N)),y=np.sort(np.random.randn(N))))
df2 =pd.DataFrame(dict(x=df1.x+0.3*np.sort(np.random.randn(N)),y=df1.y+0.1*np.sort(np.random.randn(N))))

#---------------------------------------(a)-----------------------------------------------
p1=(ggplot(df1,aes('x','y',colour='x+y'))+
geom_line(size=1)+
geom_point(shape='o',size=5)+
scale_color_distiller(name="Line",palette="Blues")+
guides(color=guide_colorbar(title="Point\nLine"))+
theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1.25,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)

#p1.save("plotnine_Advance1.pdf") 

#---------------------------------------(b)-----------------------------------------------
p1=(ggplot(df1,aes('x','y'))+
geom_line(aes(colour='x+y'),size=1)+
geom_point(aes(fill='x+y'),color="black",shape='o', size=5)+
scale_fill_distiller(name="Point",palette="YlOrRd")+
scale_color_distiller(name="Line",palette="Blues")+
theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1.25,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("plotnine_Advance2.pdf") 

#---------------------------------------(c)-----------------------------------------------
p1=(ggplot()+
geom_line(aes('x','y',colour='x+y'),df1,size=1)+
geom_point(aes('x','y',fill='x+y'),df2,color="black",shape='o', size=5)+
scale_fill_distiller(name="Point",palette="YlOrRd")+
scale_color_distiller(name="Line",palette="Blues")+
theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1.25,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)
#p1.save("plotnine_Advance3.pdf") 

