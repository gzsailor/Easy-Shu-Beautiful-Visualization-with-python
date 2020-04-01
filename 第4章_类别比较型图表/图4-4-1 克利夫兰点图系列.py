# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:13:47 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
#from plotnine.data import *
import matplotlib.pyplot as plt 

#------------------------------(a)棒棒糖图----------------------------------------------------

df=pd.read_csv('DotPlots_Data.csv')

df['sum']=df.iloc[:,1:3].apply(np.sum,axis=1)

df=df.sort_values(by='sum', ascending=True)
df['City']=df['City'].astype("category",categories= df['City'],ordered=True)

base_plot=(ggplot(df, aes('sum', 'City')) +
  geom_segment(aes(x=0, xend='sum',y='City',yend='City'))+
  geom_point(shape='o',size=3,colour="black",fill="#FC4E07")+
  theme(
    axis_title=element_text(size=12,face="plain",color="black"),
    axis_text = element_text(size=10,face="plain",color="black"),
    #legend_title=element_text(size=14,face="plain",color="black"),
   aspect_ratio =1.25,
    figure_size = (4, 4),
     dpi = 100
  ))
  
print(base_plot)
#----------------------------- (b) 克利夫兰点图 ---------------------------------------
base_plot=(ggplot(df, aes('sum', 'City')) +

  geom_point(shape='o',size=3,colour="black",fill="#FC4E07")+
  theme(
    axis_title=element_text(size=12,face="plain",color="black"),
    axis_text = element_text(size=10,face="plain",color="black"),
    #legend_title=element_text(size=14,face="plain",color="black"),
   aspect_ratio =1.25,
    figure_size = (4, 4),
     dpi = 100
  ))
  
print(base_plot)

#----------------------------------(c) 哑铃图------------------------

df=pd.read_csv('DotPlots_Data.csv')

df=df.sort_values(by='Female', ascending=True)
df['City']=df['City'].astype("category",categories= df['City'],ordered=True)
mydata=pd.melt(df,id_vars='City')

base_plot=(ggplot(mydata, aes('value','City',fill='variable')) +
  geom_line(aes(group = 'City')) +
   geom_point(shape='o',size=3,colour="black")+
  scale_fill_manual(values=("#00AFBB", "#FC4E07","#36BED9"))+
  theme(
    axis_title=element_text(size=13,face="plain",color="black"),
    axis_text = element_text(size=10,face="plain",color="black"),
    legend_title=element_text(size=12,face="plain",color="black"),
    legend_text = element_text(size=10,face="plain",color="black"),
    legend_background = element_blank(),
    legend_position = (0.75,0.2),
  aspect_ratio =1.25,
    figure_size = (4, 4),
     dpi = 100
  ))
  
print(base_plot)