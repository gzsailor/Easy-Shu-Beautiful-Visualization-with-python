# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:04:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import geopandas as gpd

import geoplot.crs as gcrs
import numpy as np
import pandas as pd
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
 
df=pd.merge(right=df_map, left=df_city,how='right',on="country")
df=gpd.GeoDataFrame(df)

#------------------------------Method:plotnine --------------------------------------------------------

base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_point(aes(x='long', y='lat',size='orange'),shape='o',colour="black",fill='#EF5439')+
           geom_text(aes(x='long', y='lat', label='city'),colour="black",size=10,nudge_y=-1.5)+
          scale_size(range=(2,9),name='price')
)
print(base_plot)


base_plot=(ggplot(df)+
           geom_map(fill='white',color='gray')+
           geom_point(aes(x='long', y='lat',size='orange',fill='orange'),shape='o',colour="black")+
           geom_text(aes(x='long', y='lat', label='city'),colour="black",size=10,nudge_y=-1.5)+
          #scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = df.orange.mean())
          scale_fill_cmap(name="YlOrRd")+
          scale_size(range=(2,9),name='price')
)
print(base_plot)


#------------------------------Method:geoplot --------------------------------------------------------
import geoplot as gplt
from shapely.geometry import Point

geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_city.long.values, df_city.lat.values)])
df_city=gpd.GeoDataFrame(df_city,geometry=geom )

ax=gplt.pointplot(
    df_city,
     hue='orange', cmap='YlOrRd', k=5,
    scale='orange', limits=(10, 25),
    edgecolors ='k',
    legend=True, legend_var='scale',
    legend_kwargs={'frameon': False,'title':'price',
                   'loc':'center','bbox_to_anchor':(1.05, 0, 0, 1)},
    legend_values=[2, 4, 6, 8, 10])

gplt.polyplot(df, facecolor='white', edgecolor='k', ax=ax)

#-----------------------------Method:basemap--------------------------------------------------
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pandas as pd

df_city=pd.read_csv("Virtual_City.csv",index_col='country') 

lat_min = 29
lat_max = 62
lon_min = 103
lon_max = 136

ax = plt.figure(figsize=(8, 6)).gca()
basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map1', name = "Country", drawbounds=True)

for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor='w', edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#添加文本信息：城名
for lat,long,country in zip(df_city['lat'],df_city['long'],df_city['city']):
    ax.text(long,lat-2,country,fontsize=12,verticalalignment="center",horizontalalignment="center")

#添加气泡
Bubble_Scale=80
scatter = ax.scatter(df_city['long'], df_city['lat'], c=df_city['orange'], s=df_city['orange']*Bubble_Scale, 
                     linewidths=0.5, edgecolors="k",cmap='YlOrRd',zorder=2)
cbar = plt.colorbar(scatter) #添加图列：colobar
cbar.set_label('orange')
 #添加图列：气泡大小
kw = dict(prop="sizes", alpha=0.6, num=5, func=lambda s: s/Bubble_Scale)
ax.legend(*scatter.legend_elements(**kw), loc="upper right", title="orange")
