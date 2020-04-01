# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:36:19 2018

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


import pandas as pd
import numpy as np
from plotnine import *


mydata=pd.read_csv("Bubble_Data.csv")
Colnames=mydata.columns.values.tolist()

base_plot=(ggplot(mydata, aes('Gas Mileage(mpg)','Power (kW)')) 
#其气泡的颜色填充由Class映射，大小由age映射
+geom_point(fill='#FE7A00',colour="black",size=8,stroke=0.2,alpha=1) #
#+scale_size_continuous(range=[3,12])
+theme_light()
+theme(
    #text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=16,face="plain",color="black"),
    axis_text = element_text(size=14,face="plain",color="black"),
    legend_text=element_text(size=14,face="plain",color="black"),
    legend_title=element_text(size=16,face="plain",color="black"),
    legend_background=element_blank(),
    #legend_position='none',
    legend_position = (0.81,0.75),
    figure_size = (8, 8),
    dpi = 50
))
print(base_plot)
#base_plot.save('Bubble1.pdf')


base_plot=(ggplot(mydata, aes('Gas Mileage(mpg)','Power (kW)',size='Weight (kg)')) 
#其气泡的颜色填充由Class映射，大小由age映射
+geom_point(fill='#EEC642',colour="black",stroke=0.2,alpha=1) #size=7,
+scale_size_continuous(range=[3,12])
+theme_light()
+theme(
    #text=element_text(size=15,face="plain",color="black"),
    axis_title=element_text(size=16,face="plain",color="black"),
    axis_text = element_text(size=14,face="plain",color="black"),
    legend_text=element_text(size=14,face="plain",color="black"),
    legend_title=element_text(size=16,face="plain",color="black"),
    legend_background=element_blank(),
    #legend_position='none',
    legend_position = (0.81,0.75),
    figure_size = (8, 8),
    dpi = 50
))
print(base_plot)
#base_plot.save('Bubble2.pdf')