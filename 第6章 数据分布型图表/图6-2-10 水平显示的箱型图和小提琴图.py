# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:03:37 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

df=pd.read_csv('Distribution_Data.csv')
df['class']=df['class'].astype("category",categories= ["n", "s", "k", "mm"],ordered=True)

#-------------------------------------(a) 箱型图--------------------------------------------
box_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_boxplot(show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+coord_flip()
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=12,colour = "black"),
       aspect_ratio =0.8,
       dpi=100,
       figure_size=(4,4)))
print(box_plot)
#box_plot.save("box_plot_coord_flip.pdf") 

#-------------------------------------------(b) 小提琴图 -------------------------------------------
violin_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_violin(show_legend=False)
+geom_boxplot(fill="white",width=0.1,show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+coord_flip()
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=12,colour = "black"),
       aspect_ratio =0.8,
       dpi=100,
       figure_size=(4,4)))
print(violin_plot)
#violin_plot.save("violin_plot_coord_flip.pdf")