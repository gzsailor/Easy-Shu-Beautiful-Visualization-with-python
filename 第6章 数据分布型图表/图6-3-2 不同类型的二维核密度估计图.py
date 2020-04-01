# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:13:45 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

N=5000
x1 = np.random.normal(1.5,1, N)
y1 =np.random.normal(1.6,1, N)
x2 = np.random.normal(2.5,1, N)
y2 =np.random.normal(2.2,1, N)

df=pd.DataFrame({'x':np.append(x1,x2),'y':np.append(y1,y2)})

#---------------------------------(a) 方块型tile.-----------------------------------
density_plot=(ggplot(df, aes('x','y')) 
+stat_density_2d (aes(fill = '..density..'),geom ="tile",contour=False)
+scale_fill_cmap(name ='Spectral_r',breaks= np.arange(0.025,0.126,0.05))
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=14,colour = "black"),
       aspect_ratio =1,
       dpi=100,
       figure_size=(4,4)))
print(density_plot)

#density_plot.save("density_plot1.pdf") 

#--------------------------------- (b) 多边形型polygon.-----------------------------------
density_plot=(ggplot(df, aes('x','y')) 
+stat_density_2d (aes(fill = '..level..'),geom ="polygon",
                  size=0.5,levels=100,contour=True)
+scale_fill_cmap(name ='Spectral_r',breaks= np.arange(0.025,0.126,0.05))
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=14,colour = "black"),
       aspect_ratio =1,
       dpi=100,
       figure_size=(4,4)))
print(density_plot)
#density_plot.save("density_plot2.pdf") 

#---------------------------------(c) 散点型-----------------------------------
density_plot=(ggplot(df, aes('x','y')) 
+geom_point(shape=".",size=1,color="black",alpha=0.3)
+stat_density_2d (aes(colour = '..level..'),geom ="polygon",
                  size=0.5,levels=10,fill="none",n=30,
                  contour=True)
+scale_color_cmap(name ='Spectral_r')
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=12,colour = "black"),
       aspect_ratio =1,
       dpi=100,
       figure_size=(4,4)))
print(density_plot)