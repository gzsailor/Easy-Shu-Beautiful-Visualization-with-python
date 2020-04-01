# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:21:27 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
#https://dawes.wordpress.com/2014/06/27/publication-ready-3d-figures-from-matplotlib/
  

import pandas as pd
import numpy as np
import seaborn as sns
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm,colors
mpl.rc('font',size=13)
#mpl.rc('font',family='serif')
#mpl.rc('axes',labelsize=14)

#plt.rcParams['grid.color'] = "w"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv("iris.data", names=names) #读取csv数据


fig = plt.figure(figsize=(8.5,8),dpi =90)  
ax =  fig.add_subplot(111,projection='3d')
#ax.set_aspect('equal','box')
ax.view_init(azim=15, elev=20)
##改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
#--------------------------------------------------------------------------------------
ax.grid(False)

ax.xaxis._axinfo['tick']['outward_factor'] = 0
ax.xaxis._axinfo['tick']['inward_factor'] = 0.4
ax.yaxis._axinfo['tick']['outward_factor'] = 0
ax.yaxis._axinfo['tick']['inward_factor'] = 0.4
ax.zaxis._axinfo['tick']['outward_factor'] = 0
ax.zaxis._axinfo['tick']['inward_factor'] = 0.4
# =============================================================================
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
# =============================================================================

ax.xaxis.pane.set_edgecolor('k')
ax.yaxis.pane.set_edgecolor('k')
ax.zaxis.pane.set_edgecolor('k')
# =============================================================================
group=np.unique(df['class'])
label=[x.split("-")[1] for x in group]
color = sns.husl_palette(len(group),h=15/360, l=.65, s=1).as_hex() 

for i in range(len(group)):
    df_temp=df[df['class']==group[i]]
    ax.scatter3D(df_temp['sepal-length'], df_temp['sepal-width'], df_temp['petal-length'],c=color[i],
                 s=100,edgecolor='k',alpha=0.95,label=label[i])

ax.set_xlabel('sepal-length')
ax.set_ylabel('sepal-width')
ax.set_zlabel('petal-length')

plt.legend(title='group',loc="center",bbox_to_anchor=(1.0, 0, 0, 1),edgecolor='none',facecolor='none')
plt.show()

#fig.savefig('三维散点图3.pdf')