# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:04:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from geopandas import GeoDataFrame
from plotnine import *

#---------------------------------(a)陆地岛屿-------------------------------------------
continents = GeoDataFrame.from_file('Virtual_Map0.shp')
base_plot=(ggplot()+ 
 geom_map(continents, aes(fill='type'))+
 scale_fill_hue(s = 1, l = 0.65, h=0.0417,color_space='husl'))

print(base_plot)

#-----------------------(b)国家.------------------------------------------
countries = GeoDataFrame.from_file('Virtual_Map1.shp')

base_plot=(ggplot()+ 
 geom_map(countries, aes(fill='country'))+
 scale_fill_hue(s = 1, l = 0.65, h=0.0417,color_space='husl'))

print(base_plot)

#continents.set_index('SP_ID', inplace=True)
#continents.plot(figsize=(6, 6),alpha=0.5, edgecolor='k')
