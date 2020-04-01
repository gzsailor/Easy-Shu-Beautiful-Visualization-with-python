# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:33:02 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 

df =pd.DataFrame(dict(segment = ["A", "B", "C","D"],
                      Alpha = [2400	,1200,	600	,250], 
                      Beta = [1000	,900,	600,	250],
                      Gamma = [400,	600	,400,	250], 
                      Delta = [200,	300	,400,	250]))
df=df.set_index('segment')
melt_df=pd.melt(df.reset_index(),id_vars=["segment"],var_name='variable',value_name='value')



df_rowsum= df.apply(lambda x: x.sum(), axis=1)

for i in df_rowsum.index:
    for j in df.columns:
        df.loc[i,j]=df.loc[i,j]/df_rowsum[i]*100
        
        
df_rowsum=df_rowsum/np.sum(df_rowsum)*100
df['xmax']= np.cumsum(df_rowsum)
df['xmin'] = df['xmax'] - df_rowsum

dfm=pd.melt(df.reset_index(), id_vars=["segment", "xmin", "xmax"],value_name="percentage")

dfm['ymax'] = dfm.groupby('segment')['percentage'].transform(lambda x: np.cumsum(x))
dfm['ymin'] = dfm.apply(lambda x: x['ymax']-x['percentage'], axis=1)

dfm['xtext']= dfm['xmin'] + (dfm['xmax'] - dfm['xmin'])/2
dfm['ytext']= dfm['ymin'] + (dfm['ymax'] - dfm['ymin'])/2

#join()函数，连接两个表格data.frame
dfm=pd.merge(left=melt_df,right=dfm,how="left",on=["segment", "variable"])


df_label=pd.DataFrame(dict(x = np.repeat(102,4), y = np.arange(12.5,100,25), label = ["Alpha","Beta","Gamma","Delta"]))

base_plot=(ggplot()+
  geom_rect(aes(ymin = 'ymin', ymax = 'ymax', xmin = 'xmin', xmax = 'xmax', fill = 'variable'),
            dfm,colour = "black") + 
  geom_text(aes(x = 'xtext', y = 'ytext',  label = 'value'),dfm ,size = 10)+
  geom_text(aes(x = 'xtext', y = 103, label = 'segment'),dfm ,size = 13)+
  geom_text(aes(x='x',y='y',label='label'),df_label,size = 10,ha  ='left')+
  scale_x_continuous(breaks=np.arange(0,101,25),limits=(0,110))+
   scale_fill_hue(s = 0.90, l = 0.65, h=0.0417,color_space='husl')+
  theme(panel_background=element_blank(),
        panel_grid_major = element_line(colour = "grey",size=.25,linetype ="dotted" ),
       panel_grid_minor = element_line(colour = "grey",size=.25,linetype ="dotted" ),
         text=element_text(size=10),
        legend_position="none",
        aspect_ratio =1.,
        figure_size = (5, 5),
        dpi = 100
  ))
  
print(base_plot)