# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:21:27 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
#https://dawes.wordpress.com/2014/06/27/publication-ready-3d-figures-from-matplotlib/
import pandas as pd
from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font',size=13)
mpl.rc('font',family='serif')
mpl.rc('axes',labelsize=14)


df=pd.read_csv('ThreeD_Scatter_Data.csv')

fig = plt.figure(figsize=(8.5,8),dpi =90)  
ax =  fig.add_subplot(1, 1, 1,projection='3d')
#ax.set_aspect('equal','box')
ax.view_init(azim=15, elev=20)

#--------------------------------------------------------------------------------------
ax.grid(False)
# Get rid of colored axes planes
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('k')
ax.yaxis.pane.set_edgecolor('k')
ax.zaxis.pane.set_edgecolor('k')

# =============================================================================
ax.xaxis._axinfo['tick']['outward_factor'] = 0
ax.xaxis._axinfo['tick']['inward_factor'] = 0.4
ax.yaxis._axinfo['tick']['outward_factor'] = 0
ax.yaxis._axinfo['tick']['inward_factor'] = 0.4
ax.zaxis._axinfo['tick']['outward_factor'] = 0
ax.zaxis._axinfo['tick']['inward_factor'] = 0.4
# =============================================================================
#--------------------------------------------------------------------------------------

scatter=ax.scatter3D(df.mph, df.Gas_Mileage, df.Power,c='#DF4736',s=df.Weight*0.25, 
             cmap='RdYlBu_r',edgecolor='k',alpha=0.8)

ax.set_xlabel('0-60 mph (sec)')
ax.set_ylabel('Gas Mileage (mpg)')
ax.set_zlabel('Power (kW)')


kw = dict(prop="sizes", num=5,c='#DF4736', func=lambda s: s/0.25)
ax.legend(*scatter.legend_elements(**kw),
                    loc="center",bbox_to_anchor=(1.0, 0, 0, 1), title="Weight")

plt.show()

#fig.savefig('三维气泡图4.pdf')
