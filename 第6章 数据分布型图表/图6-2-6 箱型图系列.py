# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:49:47 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *


freq =np.logspace(1,4,num=4-1+1,base=10,dtype='int')
df=pd.DataFrame({'class': np.repeat(['a','b','c','d'], freq), 
                 'value':np.random.normal(3, 1, sum(freq))})

box_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_boxplot(show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.1,
       dpi=100,
       figure_size=(4,4)))
print(box_plot)
#box_plot.save("box_plot3.pdf") 

box_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_boxplot(notch = True, varwidth = False,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.1,
       dpi=100,
       figure_size=(4,4)))
print(box_plot)
#box_plot.save("box_plot4.pdf") 

box_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_boxplot(notch = True, varwidth = True,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.1,
       dpi=100,
       figure_size=(4,4)))
print(box_plot)
#box_plot.save("box_plot5.pdf") 
