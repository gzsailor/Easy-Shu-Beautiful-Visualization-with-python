# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:35:06 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import numpy as np
import pandas as pd
from plotnine import *
from plotnine.data import mtcars

mat_corr=np.round(mtcars.corr(),1).reset_index()
mydata=pd.melt(mat_corr,id_vars='index',var_name='var',value_name='value')

base_plot=(ggplot(mydata, aes(x ='index', y ='var', fill = 'value',label='value')) +  
  geom_tile(colour="black") +
  geom_text(size=8,colour="white")+
  scale_fill_cmap(name ='RdYlBu_r')+
  coord_equal()+
    theme(dpi=100,figure_size=(4,4)))
print(base_plot)

mydata['AbsValue']=np.abs(mydata.value)

base_plot=(ggplot(mydata, aes(x ='index', y ='var', fill = 'value',size='AbsValue')) +  
  geom_point(shape='o',colour="black") +
  #geom_text(size=8,colour="white")+
  scale_size_area(max_size=11, guide=False) +
  scale_fill_cmap(name ='RdYlBu_r')+
  coord_equal()+
    theme(dpi=100,figure_size=(4,4)))
print(base_plot)


base_plot=(ggplot(mydata, aes(x ='index', y ='var', fill = 'value',size='AbsValue')) +  
  geom_point(shape='s',colour="black") +
  #geom_text(size=8,colour="white")+
  scale_size_area(max_size=10, guide=False) +
  scale_fill_cmap(name ='RdYlBu_r')+
  coord_equal()+
    theme(dpi=100, figure_size=(4,4)))
print(base_plot)