# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:04:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

#from geopandas import GeoDataFrame
import geopandas as gpd 
import pandas as pd
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
df=pd.merge(right=df_map, left=df_city,how='right',on="country")
df=gpd.GeoDataFrame(df)

#------------------------------Method:plotnine --------------------------------------------------------
base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_point(aes(x='long', y='lat'),shape='o',colour="black",size=6,fill='r')+
           geom_text(aes(x='long', y='lat', label='city'),colour="black",size=10,nudge_y=-1.5)+
          #scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = df.orange.mean())
          scale_fill_cmap(name="RdYlBu_r")
)
print(base_plot)

base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_label(aes(x='long', y='lat', label='city'),colour="black",size=10,fill='orange')+
          #scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = df.orange.mean())
          scale_fill_cmap(name="RdYlBu_r")
)
print(base_plot)


#------------------------------Method:geoplot --------------------------------------------------------

from shapely.geometry import Point
import geoplot as gplt
geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_city.long.values, df_city.lat.values)])
df_city=gpd.GeoDataFrame(df_city,geometry=geom )
ax=gplt.pointplot( df_city,color='red',s=10,edgecolors ='k')
gplt.polyplot(df, facecolor='white', edgecolor='k', ax=ax)



