# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:55:08 2018

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

mpl.rc('font',size=13)
mpl.rc('font',family='serif')
mpl.rc('axes',labelsize=14)
   
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


fig = plt.figure(figsize=(10,8),dpi =90)  
ax = fig.gca(projection='3d')

ax.view_init(azim=15, elev=20)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
#--------------------------------------------------------------------------------------
#ax.grid(True)
ax.xaxis._axinfo["grid"].update({"linewidth":1, "color" : "w",'linestyle':'-'})
ax.yaxis._axinfo["grid"].update({"linewidth":1, "color" : "w",'linestyle':'-'})
ax.zaxis._axinfo["grid"].update({"linewidth":1, "color" : "w",'linestyle':'-'})

ax.xaxis._axinfo['tick']['outward_factor'] = 0
ax.xaxis._axinfo['tick']['inward_factor'] = 0.4
ax.yaxis._axinfo['tick']['outward_factor'] = 0
ax.yaxis._axinfo['tick']['inward_factor'] = 0.4
ax.zaxis._axinfo['tick']['outward_factor'] = 0
ax.zaxis._axinfo['tick']['inward_factor'] = 0.4
ax.zaxis._axinfo['tick']['inward_factor'] = 0.4

ax.spines['left'].set_color('k')
ax.spines['bottom'].set_color('k')
ax.spines['top'].set_color('k')

ax.xaxis.pane.set_edgecolor('k')
ax.yaxis.pane.set_edgecolor('k')
ax.zaxis.pane.set_edgecolor('k')

#--------------------------------------------------------------------------------------
p=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='Spectral_r',alpha=1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_zlim(-1,1.5)

fig.colorbar(p, shrink=0.5,aspect=10)

plt.show()

#fig.savefig('三维曲面图.pdf')