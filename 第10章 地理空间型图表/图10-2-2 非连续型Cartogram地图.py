# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:04:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from geopandas import GeoDataFrame
import geoplot
import pandas as pd
import matplotlib.pyplot as plt

df_map = GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
 
df=pd.merge(right=df_map, left=df_city,how='right',on="country")
df=GeoDataFrame(df)

#----------------------------------orange----------------------------------------------------
ax = geoplot.cartogram(
    df,
    scale='orange', limits=(0.5, 0.9),
    #projection=gcrs.AlbersEqualArea(central_longitude=-98, central_latitude=39.5),
    hue='orange', cmap='Reds', k=10,
    linewidth=0.5,
    legend=True, legend_kwargs={'loc': 'center',
                                'bbox_to_anchor':(1.15, 0, 0, 1),
                                'title':'value',
                                'edgecolor':'white'}, legend_var='hue',
    figsize=(5, 5)
)
geoplot.polyplot(df, facecolor='lightgray', edgecolor='white', ax=ax)

#plt.title("Adult Obesity Rate by State, 2013")
#plt.savefig("cartogram_orange.pdf",bbox_inches='tight', pad_inches=0.1)

#-----------------------------------apple---------------------------------------------------
ax = geoplot.cartogram(
    df,
    scale='apple', limits=(0.5, 0.9),
    #projection=gcrs.AlbersEqualArea(central_longitude=-98, central_latitude=39.5),
    hue='apple', cmap='Reds', k=10,
    linewidth=0.5,
    legend=True, legend_kwargs={'loc': 'center',
                                'bbox_to_anchor':(1.15, 0, 0, 1),
                                'title':'value',
                                'edgecolor':'white'}, legend_var='hue',
    figsize=(5, 5)
)
geoplot.polyplot(df, facecolor='lightgray', edgecolor='white', ax=ax)

#plt.title("Adult Obesity Rate by State, 2013")
#plt.savefig("cartogram_apple.pdf",bbox_inches='tight', pad_inches=0.1)






