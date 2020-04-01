# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:22:41 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import geopandas as gpd
import geoplot.crs as gcrs
import numpy as np
import pandas as pd
import geoplot as gplt
from shapely.geometry import Point
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
from matplotlib import cm,colors


df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_city.long.values, df_city.lat.values)])
df_city=gpd.GeoDataFrame(df_city,geometry=geom )


#--------------------------------- (a)黑白沃罗诺伊图.----------------------------------------
ax1 = gplt.voronoi(
    df_city, #projection=gcrs.AlbersEqualArea(),
    clip=df_map,
    linewidth=0.5,
    #hue='orange', cmap='Reds',k=5,
    legend=False,
    edgecolor='k'
)

ax2=gplt.pointplot( df_city,color='white',s=10,edgecolors ='k',ax=ax1)#zorder=2,
gplt.polyplot(df_map, edgecolor='none', facecolor='lightgray', ax=ax1)#zorder=1,
#plt.savefig('沃罗诺伊地图2.pdf')

#--------------------------------- (b)彩色沃罗诺伊图.----------------------------------------
ax= gplt.voronoi(
    df_city, #projection=gcrs.AlbersEqualArea(),
    clip=df_map,
    hue='city', cmap='Set1',
    legend=True,k=10,
    edgecolor='w',
    alpha=0.75,
    legend_kwargs={'bbox_to_anchor':(1.15,0.5),'loc': 'center', 'edgecolor': 'none','title':'City'})

gplt.pointplot( df_city,color='white',s=10,edgecolors ='k',zorder=2,ax=ax)
gplt.polyplot(df_map, edgecolor='black', zorder=1, ax=ax)


