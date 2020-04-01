# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:55:50 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
df=pd.read_csv('Facting_Data.csv')

fig = plt.figure(figsize=(8,8),dpi =90)  
ax = fig.gca(projection='3d')
ax.view_init(azim=-70, elev=20)##改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
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
ax.xaxis.pane.set_edgecolor('k')
ax.yaxis.pane.set_edgecolor('k')
ax.zaxis.pane.set_edgecolor('k')
xs = df['X_Axis'].values
verts = []
zs = np.arange(25,65,5)
for z in zs:
    ys =df[str(z)].values
    ys[0], ys[-1] = 0, 0
    verts.append(list(zip(xs, ys)))
pal_husl = sns.husl_palette(len(zs),h=15/360, l=.65, s=1).as_hex() 

poly = PolyCollection(verts, facecolors=pal_husl,edgecolor='k')
poly.set_alpha(0.75)
ax.add_collection3d(poly, zs=zs, zdir='y')
ax.set_xlabel('X')
ax.set_xlim3d(360, 740)
ax.set_ylabel('Y')
ax.set_ylim3d(25, 60)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 15)
plt.show()
