# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:34:37 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
from geopandas import GeoDataFrame
import geoplot as gplt

#---------------------------------(a)陆地岛屿-------------------------------------------
continents = GeoDataFrame.from_file('Virtual_Map0.shp')
gplt.choropleth(
    continents[continents['type'].notnull()], hue='type',k=10,
     cmap='Set1',legend=True, figsize=(8, 4),
      legend_kwargs={'bbox_to_anchor':(1.15,0.5),'loc': 'center', 
                     'edgecolor': 'none', 'facecolor': 'none','title':'country'})

#-----------------------(b)国家.------------------------------------------
continents = GeoDataFrame.from_file('Virtual_Map1.shp')
gplt.choropleth(
    continents[continents['country'].notnull()], hue='country',k=10,
     cmap='Set1',legend=True, figsize=(8, 4),
      legend_kwargs={'bbox_to_anchor':(1.15,0.5),'loc': 'center', 
                     'edgecolor': 'none','facecolor': 'none','title':'country'})

