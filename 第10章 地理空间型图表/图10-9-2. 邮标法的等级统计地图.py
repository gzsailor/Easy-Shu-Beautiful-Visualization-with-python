# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:09:46 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import geopandas as gpd 
import pandas as pd
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
df=pd.merge(right=df_map[['country','geometry']], left=df_city[['country','orange','apple','banana','watermelon']],how='right',on="country")

df_melt=pd.melt(df,id_vars = ['country', 'geometry'])

df_melt=gpd.GeoDataFrame(df_melt)

base_plot=(ggplot()+
  geom_map(df_melt, aes(fill='value'),colour="black",size=0.25)+
  geom_text(df_city,aes(x='long', y='lat', label='country'),colour="black",size=10)+
  scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",
                       midpoint = df_city.orange.mean())+
  facet_wrap('~variable')+
  theme(strip_text = element_text(size=20,face="plain",color="black"),
        axis_title=element_text(size=18,face="plain",color="black"),
        axis_text = element_text(size=15,face="plain",color="black"),
        legend_title=element_text(size=18,face="plain",color="black"),
        legend_text = element_text(size=15,face="plain",color="black"),
        figure_size = (11, 9),
        dpi = 50))
 
print(base_plot)
