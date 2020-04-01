# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:30:18 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
import skmisc #提供loess smoothing
df=pd.read_csv('Scatter_Data.csv')
plot_loess=(ggplot( df, aes('x','y')) +
  geom_point(fill="black",colour="black",size=3,shape='o') +
  geom_smooth(method = 'loess',span=0.4,se=True,colour="#00A5FF",fill="#00A5FF",alpha=0.2)+ #(f)
  scale_y_continuous(breaks = np.arange(0, 126, 25))+
  theme(
      axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
     legend_position="none",
     aspect_ratio =1,
       figure_size = (5, 5),
       dpi = 100
       )
)

print(plot_loess)


plot_lm=(ggplot( df, aes('x','y')) +
  geom_point(fill="black",colour="black",size=3,shape='o') +
  geom_smooth(method="lm",se=True,colour="red")+ #(h)
  #geom_smooth(method = 'gam',formula='y ~s(x)')+   #(g)
  #geom_smooth(method = 'loess',span=0.4,se=True,colour="#00A5FF",fill="#00A5FF",alpha=0.2)+ #(f)
  scale_y_continuous(breaks = np.arange(0, 126, 25))+
  theme(
      axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
     legend_position="none",
     aspect_ratio =1,
       figure_size = (5, 5),
       dpi = 100
       )
)

print(plot_lm)

plot_glm=(ggplot( df, aes('x','y')) +
  geom_point(fill="black",colour="black",size=3,shape='o') +
  geom_smooth(method="glm",se=True,colour="red")+ #(h)
  #geom_smooth(method = 'gam')+   #(g)
  #geom_smooth(method = 'loess',span=0.4,se=True,colour="#00A5FF",fill="#00A5FF",alpha=0.2)+ #(f)
  scale_y_continuous(breaks = np.arange(0, 126, 25))+
  theme(
      axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
     legend_position="none",
     aspect_ratio =1,
       figure_size = (5, 5),
       dpi = 100
       )
)

print(plot_glm)
