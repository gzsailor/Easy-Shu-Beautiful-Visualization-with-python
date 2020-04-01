# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:08:03 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import pandas as pd
from plotnine import *

#----------------------------------(a)离散点状地图--------------------------------------------------------

df_map = gpd.GeoDataFrame.from_file('Virtual_Map0.shp')

long_mar=np.arange(105,135, 0.6)
lat_mar=np.arange(30,60, 0.8)
X,Y=np.meshgrid(long_mar,lat_mar)
df_grid =pd.DataFrame({'long':X.flatten(),'lat':Y.flatten()})

geom  = gpd.GeoSeries([Point(x, y) for x, y in zip(df_grid.long.values, df_grid.lat.values)])
df_grid=gpd.GeoDataFrame(df_grid,geometry=geom)


inter_point=df_map['geometry'].intersection(df_grid['geometry'].unary_union).tolist()

point_x=[]
point_y=[]
for i in range(len(inter_point)):
    if (str(type(inter_point[i]))!="<class 'shapely.geometry.point.Point'>"):
        point_x=point_x+[item.x for item in inter_point[i]]
        point_y=point_y+[item.y for item in inter_point[i]]
    else:
        point_x=point_x+[inter_point[i].x]
        point_y=point_y+[inter_point[i].y]

df_pointmap =pd.DataFrame({'long':point_x,'lat':point_y})

plot_base=(ggplot() +
           geom_map(df_map,fill='white',color='k')+
           geom_point(df_pointmap,aes(x='long',y='lat'),fill='k',size=3,shape='o',stroke=0.1))
print(plot_base)

#----------------------------------(b)统计直方的点状地图.--------------------------------------------------------

df_huouse=pd.read_csv("Virtual_huouse.csv") 

plot_base=(ggplot() +
           geom_map(df_map,fill='white',color='k')+
           geom_point(df_huouse,aes(x='long',y='lat'),fill='k',size=1,shape='o',stroke=0.1))
print(plot_base)


long_mar=np.arange(105,135+0.6, 0.6)
lat_mar=np.arange(30,60+0.8, 0.8)
hist, xedges, yedges = np.histogram2d(df_huouse.long.values, df_huouse.lat.values, (long_mar, lat_mar))  
long_mar=np.arange(105,135, 0.6)
lat_mar=np.arange(30,60, 0.8)
Y,X=np.meshgrid(lat_mar,long_mar)
df_gridmap =pd.DataFrame({'long':X.ravel(),'lat':Y.ravel(),'count':hist.ravel()})
#plt.imshow(hist)
df_pointmap=pd.merge(df_pointmap,df_gridmap,how='left',on=['long','lat'])

plot_base=(ggplot() +
           geom_map(df_map,fill='white',color='none')+
           geom_point(df_pointmap,aes(x='long',y='lat',fill='count'),size=3,shape='o',stroke=0.1)+
           scale_fill_cmap(name='Spectral_r'))
print(plot_base)

#----------------------------------------basemap-------------------------------------------
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

lat_min = 29
lat_max = 62
lon_min = 103
lon_max = 136

ax = plt.figure(figsize=(8, 6)).gca()
basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map1', name = "Country", drawbounds=False)

for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor='w', edgecolor='w')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#添加带颜色映射的散点
scatter = ax.scatter(df_pointmap['long'], df_pointmap['lat'], c=df_pointmap['count'], 
                     s=40, linewidths=0.25, edgecolors="k",cmap='Spectral_r',zorder=2)
cbar = plt.colorbar(scatter)
cbar.set_label('Count')
