# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:05:20 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
from plotnine import *
#from plotnine.data import *
import matplotlib.pyplot as plt 

N=100
df=pd.DataFrame(dict(group=np.repeat([1,2], N*2),
                     y=np.append(np.append(np.random.normal(5,1,N),np.random.normal(2,1,N)),
                                 np.append(np.random.normal(1,1,N),np.random.normal(3,1,N))),
                     x=np.tile(["A","B","A","B"], N)))

#------------------------------------(a)#未调整箱型图和抖动散点图的间距--------------------                     
base_plot=(ggplot(df, aes(x='x', y='y',fill='factor(group)' )) 
  +geom_boxplot(outlier_size  = 0,colour='k') 
  +geom_jitter(aes(group='factor(group)'),
              shape = 'o', alpha = 0.5) 
   +scale_fill_manual(values = ("#F8766D","#00BFC4"),guide = guide_legend(title='Group'))     
  +theme_matplotlib()
  +theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
         legend_position=(0.8,0.8),
       aspect_ratio =1.05,
       figure_size = (5,5),
       dpi = 100
       )
  )

print(base_plot)
#base_plot.save('位置调整1.pdf')

#------------------------------(b)#调整抖动散点图的间距----------------------------------
base_plot=(ggplot(df, aes(x='x', y='y',fill='factor(group)' )) 
  +geom_boxplot(outlier_size  = 0,colour='k') 
  +geom_jitter(aes(group='factor(group)'),
              shape = 'o', alpha = 0.5, position=position_jitterdodge()) 
  +scale_fill_manual(values = ("#F8766D","#00BFC4"),guide = guide_legend(title='Group'))     
  +theme_matplotlib()
  +theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       legend_position=(0.8,0.8),
       aspect_ratio =1.05,
       figure_size = (5,5),
       dpi = 100
       )
  )

print(base_plot)
#base_plot.save('位置调整2.pdf')

#-----------------------------(c)#同时调整箱型图和抖动散点图的间距-----------------------
base_plot=(ggplot(df, aes(x='x', y='y',fill='factor(group)' )) 
  +geom_boxplot(position = position_dodge(0.85),outlier_size  = 0,colour='k') 
  +geom_jitter(aes(group='factor(group)'),
              shape = 'o', alpha = 0.5, 
              position=position_jitterdodge(dodge_width = 0.85)) 
  +scale_fill_manual(values = ("#F8766D","#00BFC4"),guide = guide_legend(title='Group'))                             
  +theme_matplotlib()
  +theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
         legend_position=(0.8,0.8),
       aspect_ratio =1.05,
       figure_size = (5,5),
       dpi = 100
       )
  )

print(base_plot)
#base_plot.save('位置调整3.pdf')