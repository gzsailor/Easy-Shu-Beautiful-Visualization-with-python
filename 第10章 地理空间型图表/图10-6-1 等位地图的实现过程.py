# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:26:39 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import geopandas as gpd
import geoplot.crs as gcrs
import pandas as pd
import geoplot as gplt
from shapely.geometry import Point
import matplotlib.pyplot as plt 

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_huouse=pd.read_csv("Virtual_huouse.csv") 
 

geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_huouse.long.values, df_huouse.lat.values)])
df_huouse=gpd.GeoDataFrame(df_huouse,geometry=geom)

#--------------------------------(a)点描法地图--------------------------------------------------
ax = gplt.pointplot(df_huouse,color='#54AEAD',s=3,edgecolors ='none',
                  figsize=(10, 6))#projection=gcrs.AlbersEqualArea()
gplt.polyplot(df_map, facecolor='white', edgecolor='k', ax=ax)
#plt.savefig('热力地图1.pdf')


#-------------------------------(b)二维核密度估计热力地图. ---------------------------------------------------
ax = gplt.kdeplot(df_huouse, cmap='Spectral_r', shade=True, clip=df_map,#gridsize=100,
                  figsize=(10, 6),cbar=True,cbar_kws={'shrink':0.75})#projection=gcrs.AlbersEqualArea()
gplt.polyplot(df_map, facecolor='none', edgecolor='k', ax=ax,zorder=1)
#plt.savefig('热力地图2.pdf')

#-----------------------------Method:basemap--------------------------------------------------
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib import cm,colors
import numpy as np

df_huouse=pd.read_csv("Virtual_huouse.csv") 

lat_min = 29
lat_max = 62
lon_min = 103
lon_max = 136

fig = plt.figure(figsize=(8, 6))
ax = fig.gca()
basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map1', name = "Country", drawbounds=True)

for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor='w', edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#添加散点
ax.scatter(df_huouse['long'], df_huouse['lat'],
                     c='none',s=15, linewidths=0.5, edgecolors="k",zorder=2)

