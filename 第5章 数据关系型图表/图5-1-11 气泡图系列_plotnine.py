# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:17:16 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import mtcars

#---------------------------------(c) 带数据标签的气泡图 -------------------------------
base_plot=(ggplot(mtcars, aes(x='wt',y='mpg'))+
   geom_point(aes(size='disp',fill='disp'),shape='o',colour="black",alpha=0.8)+ 
# 绘制气泡图，颜色填充和面积大小都映射到“disp”
   scale_fill_gradient2(low="#377EB8",high="#E41A1C",
                        limits = (0,np.max(mtcars.disp)), 
                        midpoint = np.mean(mtcars.disp))+ #设置填充颜色映射主题(Colormap)
  scale_size_area(max_size=12)+ # 设置显示的气泡图气泡最大面积
  geom_text(label = mtcars.disp,nudge_x =0.3,nudge_y =0.3)+ # 添加数据标签disp”
  theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1.2,
       figure_size = (5,5),
       dpi = 100
       )
  )
print(base_plot)


#---------------------------- (d) 方块状的气泡图--------------------------------------
base_plot=(ggplot(mtcars, aes(x='wt',y='mpg'))+
   geom_point(aes(size='disp',fill='disp'),shape='s',colour="black",alpha=0.8)+ 
# 绘制气泡图，颜色填充和面积大小都映射到“disp”
   scale_fill_gradient2(low="#377EB8",high="#E41A1C",
                        limits = (0,np.max(mtcars.disp)), 
                        midpoint = np.mean(mtcars.disp))+ #设置填充颜色映射主题(Colormap)
  scale_size_area(max_size=12)+ # 设置显示的气泡图气泡最大面积
  #geom_text(label = mtcars.disp,nudge_x =0.3,nudge_y =0.3)+ # 添加数据标签disp”
  theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1.2,
       figure_size = (5,5),
       dpi = 100
       )
  )
print(base_plot)