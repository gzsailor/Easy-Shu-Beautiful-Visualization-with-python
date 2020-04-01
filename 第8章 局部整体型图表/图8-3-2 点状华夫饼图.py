# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:07:39 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import mpg

#---------------------------------------- (b)百分比堆积型.-----------------------------------
nrows=10
categ_table=(np.round(pd.value_counts(mpg['class'] ) * ((nrows*nrows)/(len(mpg['class']))),0)).astype(int)
sort_table=categ_table.sort_values(ascending=False)
a = np.arange(1,nrows+1,1)
b = np.arange(1,nrows+1,1)
X,Y=np.meshgrid(a,b)
df_grid =pd.DataFrame({'x':X.flatten(),'y':Y.flatten()})
df_grid['category']=pd.Categorical(np.repeat(sort_table.index,sort_table[:]),
                 categories=sort_table.index, ordered=False)

#---------------------------------块状----------------------------------------
base_plot=(ggplot(df_grid, aes(x = 'x', y = 'y', fill = 'category')) + 
  geom_tile(color = "white", size = 0.25) +
  #geom_point(color = "black",shape='o',size=13) + 
  coord_fixed(ratio = 1)+
  scale_fill_brewer(type='qual',palette="Set2")+
  theme_void()+
  theme(panel_background  = element_blank(),
    legend_position = "right",
    aspect_ratio =1,
    figure_size = (5, 5),
    dpi = 100))
print(base_plot)

#---------------------------------点状----------------------------------------
base_plot=(ggplot(df_grid, aes(x = 'x', y = 'y', fill = 'category')) + 
  #geom_tile(color = "white", size = 0.25) +
  geom_point(color = "black",shape='o',size=13) + 
  coord_fixed(ratio = 1)+
  #scale_x_continuous(trans = 'reverse') +#expand = c(0, 0),
  #scale_y_continuous(trans = 'reverse') +#expand = c(0, 0),
  scale_fill_brewer(type='qual',palette="Set2")+
  theme(#panel.border = element_rect(fill=NA,size = 2),
    panel_background  = element_blank(),
    #axis.text = element_blank(),
    #axis.title = element_blank(),
    #axis.ticks = element_blank(),
    # legend.title = element_blank(),
    legend_position = "right",
    aspect_ratio =1,
       figure_size = (5, 5),
       dpi = 100
       )
  )

print(base_plot)
#-----------------------------------------(a)堆积型------------------------------------------------------------------------

categ_table=(np.round(pd.value_counts(mpg['class'] ),0)).astype(int)

sort_table=categ_table.sort_values(ascending=False)

ndeep= 10
a = np.arange(1,ndeep+1,1)
b = np.arange(1,np.ceil(sort_table.sum()/ndeep)+1,1)
X,Y=np.meshgrid(a,b)
df_grid =pd.DataFrame({'x':X.flatten(),'y':Y.flatten()})


category=np.repeat(sort_table.index,sort_table[:])
df_grid=df_grid.loc[np.arange(0,len(category)),:]

df_grid['category']=pd.Categorical(category,
                     categories=sort_table.index, 
                     ordered=False)

#---------------------------------块状----------------------------------------

base_plot=(ggplot(df_grid, aes(x = 'y', y = 'x', fill = 'category')) + 
  geom_tile(color = "white", size = 0.25) +
  #geom_point(color = "black",shape='o',size=7) + 
  coord_fixed(ratio = 1)+
   xlab("1 square = 100")+
   ylab("")+
  scale_fill_brewer(type='qual',palette="Set2")+
  theme(panel_background  = element_blank(),
       legend_position = "right",
       figure_size = (7, 7),
       dpi = 100))

print(base_plot)

#---------------------------------点状----------------------------------------
base_plot=(ggplot(df_grid, aes(x = 'y', y = 'x', fill = 'category')) + 
  #geom_tile(color = "white", size = 0.25) +
  geom_point(color = "black",shape='o',size=7) + 
  coord_fixed(ratio = 1)+
   xlab("1 square = 100")+
   ylab("")+
  scale_fill_brewer(type='qual',palette="Set2")+
  theme(panel_background  = element_blank(),
       legend_position = "right",
       figure_size = (7, 7),
       dpi = 100))

print(base_plot)
















