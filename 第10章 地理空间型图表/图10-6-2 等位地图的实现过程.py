# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:30:40 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import geopandas as gpd
import geoplot.crs as gcrs
import pandas as pd
import geoplot as gplt
from shapely.geometry import Point
import matplotlib.pyplot as plt 
import scipy.stats as st
import numpy as np
from plotnine import *

df_map = gpd.GeoDataFrame.from_file('Virtual_Map1.shp')
df_huouse=pd.read_csv("Virtual_huouse.csv") 

long_mar=np.arange(105,135, 0.2)
lat_mar=np.arange(30,60, 0.2)
xx,yy=np.meshgrid(long_mar,lat_mar)
df_grid =pd.DataFrame(dict(long=xx.ravel(),lat=yy.ravel()))

geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_grid.long.values, df_grid.lat.values)])
df_geogrid=gpd.GeoDataFrame(df_grid,geometry=geom)
inter_point=df_map['geometry'].intersection(df_geogrid['geometry'].unary_union).tolist()

point_x=[]
point_y=[]
for i in range(len(inter_point)):
    if (str(type(inter_point[i]))!="<class 'shapely.geometry.point.Point'>"):
        point_x=point_x+[item.x for item in inter_point[i]]
        point_y=point_y+[item.y for item in inter_point[i]]
    else:
        point_x=point_x+[inter_point[i].x]
        point_y=point_y+[inter_point[i].y]

df_pointmap =pd.DataFrame(dict(long=point_x,lat=point_y))

positions =np.vstack([df_pointmap.long.values, df_pointmap.lat.values])
values = np.vstack([df_huouse.long.values, df_huouse.lat.values])
kernel = st.gaussian_kde(values)
df_pointmap['density'] =kernel(positions)

#----------------------------------(a)点描法地图-----------------------------------------------------
plot_base=(ggplot() +
           geom_tile(df_pointmap,aes(x='long',y='lat',fill='density'),size=0.1)+
           geom_map(df_map,fill='none',color='k',size=0.5)+
           scale_fill_cmap(name='Spectral_r'))
print(plot_base)
#plot_base.save('热力地图3.pdf')


#----------------------------------(b)二维核密度估计热力图---------------------------------------------
plot_base=(ggplot() +
           geom_map(df_map,fill='w',color='k',size=0.5)+
           geom_point(df_huouse,aes(x='long',y='lat'),fill='k',size=2,color='k',stroke=0.1,alpha=0.5))
print(plot_base)
#plot_base.save('热力地图4.pdf')


#-----------------------------------------Method:basemap--------------------------------------------------
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

df_grid['group']=[str(x)+'_'+str(y) for x,y in zip(df_grid['long'],df_grid['lat'])]

df_pointmap['group']=[str(x)+'_'+str(y) for x,y in zip(df_pointmap['long'],df_pointmap['lat'])]
df_grid=pd.merge(df_grid,df_pointmap[['group','density']],how='left',on='group')

lat_min = 29; lat_max = 62; lon_min = 103; lon_max = 136

ax=plt.figure(figsize=(8, 6)).gca()
basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map1', name = "Country", drawbounds=True)

for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor='none', edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#scatter=ax.scatter(df_pointmap['long'], df_pointmap['lat'], c=df_pointmap['density'], s=15, 
#                     linewidths=0.5, edgecolors="none",cmap='Spectral_r',zorder=1)
#basemap.hexbin(df_huouse['long'], df_huouse['lat'],gridsize=20, mincnt=1, cmap='Spectral_r')
cs=basemap.pcolormesh(xx,yy, 
                   data=df_grid['density'].values.reshape((len(long_mar),len(lat_mar))),
                   cmap='Spectral_r')  

ct=basemap.contour(xx, yy, 
                     data=df_grid['density'].values.reshape((len(long_mar),len(lat_mar))),
                     colors='w')#np.arange(0, 0.008, 0.001),cmap = plt.cm.Spectral_r
ax.clabel(ct, inline=True, fontsize=10,colors='k')
cbar = basemap.colorbar(cs,location='right')
cbar.set_label('Desnity')         