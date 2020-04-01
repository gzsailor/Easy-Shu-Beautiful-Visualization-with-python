# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:52:29 2019

@author:Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

df=pd.read_csv('Distribution_LargeData.csv')

#-----------------------------------(a) 不同数据量的正态分布---------------------------
box_plot=(ggplot(df,aes(x='class',y="value",fill="class"))
+geom_boxplot(show_legend=False)
+scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')
+theme_matplotlib()
+theme(#legend_position='none',
       aspect_ratio =1.05,
       dpi=100,
       figure_size=(4,4)))
print(box_plot)
#box_plot.save("boxenplot3.pdf") 

#-----------------------------------(b) 相同大数据的不同数据分布---------------------------
df['class']=df['class'].astype("category",categories= ["n", "s", "k", "mm"],ordered=True)
fig = plt.figure(figsize=(4,4.5))
sns.boxenplot(x="class", y="value", data=df,linewidth =0.2,
                   palette=sns.husl_palette(4, s = 0.90, l = 0.65, h=0.0417))
#fig.savefig('boxenplot2.pdf') 