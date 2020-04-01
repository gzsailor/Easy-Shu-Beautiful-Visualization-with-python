# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:31:34 2020

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import seaborn as sns

lat_min = 29
lat_max = 62
lon_min = 103
lon_max = 136


fig = plt.figure(figsize=(8, 6))
ax = fig.gca()
#plt.subplots_adjust(left=0.12, right=0.98, top=0.75, bottom=0)
basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map0', name = "Country", drawbounds=True)

#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_color('none')
#ax.spines['bottom'].set_color('none')
df_mapData = pd.DataFrame(basemap.Country_info)
country=np.unique(df_mapData['type'])
color = sns.husl_palette(len(country),h=15/360, l=.65, s=1).as_hex()
colors = dict(zip(country.tolist(),color))


for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor=colors[info['type']], edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0]) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1]) #画纬度线

patches = [ mpatches.Patch(color=color[i], label=country[i]) for i in range(len(country)) ]
ax.legend(handles=patches, bbox_to_anchor=[1.25,0.5],
          borderaxespad=0,loc="center right",markerscale=1.3,
          edgecolor='none',facecolor='none',fontsize=10,title='type')


#--------------------------------------------------------------------------------------
ax = plt.figure(figsize=(6, 6)).gca()

basemap = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min,urcrnrlat=lat_max,
                  projection='cyl',lon_0 = 120,lat_0 = 50,ax = ax)
basemap.readshapefile(shapefile = 'Virtual_Map1', name = "Country", drawbounds=True)

df_mapData = pd.DataFrame(basemap.Country_info)
country=np.unique(df_mapData['country'])
color = sns.husl_palette(len(country),h=15/360, l=.65, s=1).as_hex()
colors = dict(zip(country.tolist(),color))

for info, shape in zip(basemap.Country_info, basemap.Country): 
        poly = Polygon(shape, facecolor=colors[info['country']], edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#添加图例
patches = [ mpatches.Patch(color=color[i], label=country[i]) for i in range(len(country)) ]
ax.legend(handles=patches, bbox_to_anchor=[1.25,0.5],
          borderaxespad=0,loc="center right",markerscale=1.3,
          edgecolor='none',facecolor='none',fontsize=10,title='country')

#------------------------------------Method：GeoDataFrame--------------------------------------------------
from geopandas import GeoDataFrame
import matplotlib.patches as mpathes
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from matplotlib import cm,colors

basemap= GeoDataFrame.from_file('Virtual_Map1.shp')

country=np.unique(basemap['country'])

fig = plt.figure(figsize=(8, 6))
ax = fig.gca()
#plt.subplots_adjust(left=0.12, right=0.98, top=0.75, bottom=0)

patches=[]
for shape in basemap['geometry']: 
    poly = mpathes.Polygon(list(shape.exterior.coords))
    patches.append(poly) 

#color_value =[x*y for x,y in zip(df['x'],df['y'])]
collection = PatchCollection(patches, facecolor='b',alpha=1,edgecolor='k',linewidth=1)#,
#collection.set_array()
ax.add_collection(collection)
plt.axis('equal')
plt.show()
