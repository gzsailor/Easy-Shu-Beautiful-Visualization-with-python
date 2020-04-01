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
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl


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

#------------------------------------------------------------------------------------------

df_huouse=pd.read_csv("Virtual_huouse.csv") 


long_mar=np.arange(105,135+0.6, 0.6)
lat_mar=np.arange(30,60+0.8, 0.8)
hist, xedges, yedges = np.histogram2d(df_huouse.long.values, df_huouse.lat.values, (long_mar, lat_mar))  
long_mar=np.arange(105,135, 0.6)
lat_mar=np.arange(30,60, 0.8)
Y,X=np.meshgrid(lat_mar,long_mar)
df_gridmap =pd.DataFrame({'long':X.ravel(),'lat':Y.ravel(),'count':hist.ravel()})
#plt.imshow(hist)
df_gridmap=pd.merge(df_gridmap,df_pointmap,how='left',on=['long','lat'])


#------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(7,8),dpi =150)
#ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')
ax.view_init(azim=50, elev=20)##改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
ax.grid(False)

ax.xaxis._axinfo['tick']['outward_factor'] = 0
ax.xaxis._axinfo['tick']['inward_factor'] = 0.4
ax.yaxis._axinfo['tick']['outward_factor'] = 0
ax.yaxis._axinfo['tick']['inward_factor'] = 0.4
ax.zaxis._axinfo['tick']['outward_factor'] = 0
ax.zaxis._axinfo['tick']['inward_factor'] = 0.4
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('none')
ax.yaxis.pane.set_edgecolor('none')
ax.zaxis.pane.set_edgecolor('none')


ax.zaxis.line.set_visible(False)
ax.set_zticklabels([])
ax.set_zticks([])

dx=df_gridmap.long.values
dy=df_gridmap.lat.values
dz=df_gridmap['count'].values

plt.xlim(min(dx),max(dx))
plt.ylim(min(dy),max(dy))
plt.margins(0,0,0)

ax.set_xlabel( "long")
ax.set_ylabel("lat")
#ax.set_zlabel("count")

zpos = 0

# Construct arrays with the dimensions for the 16 bars.
#dx = dy = 0.5 * np.ones_like(zpos)
#$dz = hist.ravel()

colors = cm.Reds(dz / float(max(dz)))

ax.bar3d(dx, dy, zpos, 0.5, 0.5, dz, color=colors,
         alpha=1,edgecolor='k',linewidth=0.1,zsort='average')

ax2 = fig.add_axes([0.85, 0.35, 0.025, 0.15])
cmap = mpl.cm.Reds
norm = mpl.colors.Normalize(vmin=0, vmax=1)
bounds = np.arange(min(dz),max(dz),2)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,norm=norm,boundaries=bounds,
ticks=np.arange(min(dz),max(dz),2),spacing='proportional',label='count')
#fig.savefig('三维统计直方地图1.pdf')
plt.show()