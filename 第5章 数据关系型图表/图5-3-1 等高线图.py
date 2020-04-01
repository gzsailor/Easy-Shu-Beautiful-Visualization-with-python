# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:24:59 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
#from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
from matplotlib.pyplot import figure, show, rc

mpl.rc('font',size=10)

df=pd.DataFrame(np.loadtxt('等高线.txt'))
df=df.reset_index()


ngridx = 100
ngridy = 200

xi = np.linspace(0, 300, ngridx)
yi = np.linspace(0, 200, ngridy)

# Perform linear interpolation of the data (x,y)
# on a grid defined by (xi,yi)
triang = tri.Triangulation(map_df['index'], map_df['var'])
interpolator = tri.LinearTriInterpolator(triang, map_df['value'])
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

#-------------------------------------(a)热力分布图 --------------------------------------------------------
fig, ax = plt.subplots(figsize=(5,4),dpi =90)  

ax.contour(xi, yi, zi, levels=100, linewidths=0.5, colors='none')
cntr = ax.contourf(xi, yi, zi, levels=100, cmap="Spectral_r")

cbar=fig.colorbar(cntr,ax=ax,label="value")
cbar.set_ticks(np.arange(500,3500,500))
#fig.savefig('等高线图1.pdf')

#------------------------------------(b) 等高线图----------------------------------------------
# Note that scipy.interpolate provides means to interpolate data on a grid
# as well. The following would be an alternative to the four lines above:
#from scipy.interpolate import griddata
#zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')
fig, ax = plt.subplots(figsize=(5,4),dpi =90)  

ax.contour(xi, yi, zi, levels=10, linewidths=0.5, colors='k')
cntr = ax.contourf(xi, yi, zi, levels=10, cmap="Spectral_r")

fig.colorbar(cntr,ax=ax,label="value")
#plt.plot(x, y, 'ko', ms=3)
#ax.axis((-2, 2, -2, 2))
#ax.set_title('' %(npts, ngridx * ngridy))
#fig.savefig('等高线图2.pdf') 
#------------------------------------(c) 带标签的等高线图-----------------------------------------------
fig, ax = plt.subplots(figsize=(5,4),dpi =90)  

CS=ax.contour(xi, yi, zi, levels=10, linewidths=0.5, colors='k')
cntr = ax.contourf(xi, yi, zi, levels=10, cmap="Spectral_r")
fig.colorbar(cntr,ax=ax,label="value")                
CS.levels = [int(val) for val in cntr.levels]
ax.clabel(CS, CS.levels, fmt='%.0f', inline=True,  fontsize=10)
#fig.savefig('等高线图3.pdf')