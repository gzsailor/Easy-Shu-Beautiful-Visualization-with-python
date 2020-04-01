# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:56:34 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import geopandas as gpd 
import pandas as pd
from plotnine import *

Scale=3
width=1.1

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv")
selectCol=["orange","apple","banana","watermelon"]
MaxH=df_city.loc[:,selectCol].max().max()

df_city.loc[:,selectCol]=df_city.loc[:,selectCol]/MaxH*Scale

df_city=pd.melt(df_city.loc[:,['lat','long','group','city']+selectCol],
              id_vars=['lat','long','group','city'])

df_city['hjust1']=df_city.transform(lambda x: -width if x['variable']=="orange" 
                                              else -width/2 if x['variable']=="apple"
                                              else 0 if x['variable']=="banana" else width/2 ,axis=1)

df_city['hjust2']=df_city.transform(lambda x: -width/2 if x['variable']=="orange" 
                                              else 0 if x['variable']=="apple"
                                              else width/2 if x['variable']=="banana" else width ,axis=1)

base_plot=(ggplot()+
           geom_map(df_map,fill='white',color='gray')+
            geom_rect(df_city, aes(xmin = 'long +hjust1', xmax = 'long+hjust2',
                      ymin = 'lat', ymax = 'lat + value' , fill= 'variable'), 
                      size =0.25, colour ="black", alpha = 1)+
           geom_text(df_city.drop_duplicates('city'),aes(x='long', y='lat', label='city'),
                     colour="black",size=10,nudge_y=-1.25)+
          scale_fill_hue(s = 1, l = 0.65, h=0.0417,color_space='husl'))
print(base_plot)
