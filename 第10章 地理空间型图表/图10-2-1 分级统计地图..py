# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:04:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from geopandas import GeoDataFrame
import geoplot
import pandas as pd
from plotnine import *
df_map = GeoDataFrame.from_file('Virtual_Map1.shp')
df_city=pd.read_csv("Virtual_City.csv") 
 
df=pd.merge(right=df_map, left=df_city,how='right',on="country")
df=GeoDataFrame(df)

#-----------------------------Method:plotnine------------------------------------
base_plot=(ggplot(df)+
           geom_map(aes(fill='orange'))+
           geom_text(aes(x='long', y='lat', label='country'),colour="black",size=10)+
          scale_fill_gradient2(low="#00A08A",mid="white",high="#FF0000",midpoint = df.orange.mean())
)
print(base_plot)

#-----------------------Method:geoplot---------------------------------------
#continents.set_index('SP_ID', inplace=True)
#continents.plot(figsize=(6, 6),alpha=0.5, edgecolor='k')
geoplot.choropleth(
    df, hue=df['orange'],cmap='RdYlBu_r',legend=True, figsize=(8, 4))

#--------------------Method:basemap-------------------------------------------
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib import cm,colors
import matplotlib as mpl
import pandas as pd
import numpy as np

df_city=pd.read_csv("Virtual_City.csv",index_col='country') 
n_colors=100
color=[colors.rgb2hex(x) for x in cm.get_cmap( 'RdYlBu_r',n_colors)(np.linspace(0, 1, n_colors))]
dz_min=df_city['orange'].min()
dz_max=df_city['orange'].max()
df_city['value']=(df_city['orange']-dz_min)/(dz_max-dz_min)*99   
df_city['color']=[color[int(i)] for i in df_city['value']]

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
        poly = Polygon(shape, facecolor=df_city.loc[info['country'],'color'], edgecolor='k')
        ax.add_patch(poly) 

basemap.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0],zorder=0) #画经度线
basemap.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1],zorder=0) #画纬度线

#添加文本信息：国名
for lat,long,country in zip(df_city['lat'],df_city['long'],df_city.index):
    ax.text(long,lat,country,fontsize=12,verticalalignment="center",horizontalalignment="center")

#添加图例：colorbar
ax2 = fig.add_axes([0.85, 0.35, 0.025, 0.3])

cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=mpl.cm.RdYlBu_r,
                                boundaries=np.arange(dz_min,dz_max,0.1),
                                ticks=np.arange(0,10,2),
                                label='Orange')
cb2.ax.tick_params(labelsize=15)