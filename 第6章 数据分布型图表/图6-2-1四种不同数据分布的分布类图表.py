# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:30:46 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
from plotnine import *
df=pd.read_csv('Distribution_Data.csv')
df['class']=df['class'].astype("category",categories= ["n", "s", "k", "mm"],ordered=True)

#-------------------------------------------核密度估计图-------------------------------------------
density_plot=(ggplot(df,aes(x="value",fill="class"))
+geom_density(alpha=1)
+facet_grid('class~.')
#+scale_fill_brewer(palette  =6,type ="qualitative"))
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_light()
+theme(aspect_ratio =0.25,
       dpi=100,
       figure_size=(3,4)))
print(density_plot)
#density_plot.save("density_plot.pdf")

#-------------------------------------------统计直方图-------------------------------------------
histogram_plot=(ggplot(df,aes(x="value",fill="class"))
+geom_histogram(alpha=1,colour="black",bins=30,size=0.2)
+facet_grid('class~.')
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_light()
+theme(aspect_ratio =0.25,
       dpi=100,
       figure_size=(3,4)))
print(histogram_plot)
#histogram_plot.save("histogram_plot.pdf")
