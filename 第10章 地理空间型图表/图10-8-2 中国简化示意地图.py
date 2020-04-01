# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:07:15 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


import pandas as pd
import numpy as np
from plotnine import *
from pylab import mpl


import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
from matplotlib.collections import PatchCollection

from matplotlib import cm,colors

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

#-------------------------------(c)六角形.----------------------------------------------
#file = open('China_HexMap.csv',  errors='ignore') #encoding='utf-8', 
df=pd.read_csv('China_HexMap.csv',encoding='gb2312')
#file.close()  # 关闭文件

base_plot=(ggplot()+
geom_polygon(df,aes(x='x',y='y',group='Province'),colour="black",size=0.25,fill='w')+ #中国地图
geom_text(df.drop_duplicates('Province'),aes(x='Centerx', y='Centery-0.01',label='Province'),size=14,family='SimHei')+
#+scale_fill_cmap( name="Spectral_r")
#+theme_matplotlib()
theme(
    axis_title=element_text(size=18,face="plain",color="black"),
    axis_text = element_text(size=15,face="plain",color="black"),
    figure_size = (10, 10),
    dpi = 50))
print(base_plot)



fig = plt.figure(figsize=(6, 6))
ax = fig.gca()
patches = []
for Province in np.unique(df['Province']):
    df_Province=df[df['Province']==Province]
    rect = mpathes.Polygon([(x,y) for x,y in zip(df_Province['x'],df_Province['y'])])
    patches.append(rect)
    ax.text(df_Province['Centerx'].values[0],df_Province['Centery'].values[0],
            df_Province['Province'].values[0],fontsize=12,
            verticalalignment="center",horizontalalignment="center")
    
collection = PatchCollection(patches, facecolor='w',edgecolor='k',linewidth=1)
ax.add_collection(collection)
plt.axis('equal')
plt.show()


# =============================================================================
# color_value =[x*y for x,y in zip(df['x'],df['y'])]
# collection = PatchCollection(patches, alpha=1,cmap=plt.cm.Spectral_r,edgecolor='k',linewidth=1)#facecolor='w',
# collection.set_array(np.array(color_value))
# ax.add_collection(collection)
# plt.axis('equal')
# plt.show()
# =============================================================================

#------------------------------- (a)矩形. (b)圆圈.------------------------------------
#file = open('China_MatrixMap.csv',  errors='ignore') #encoding='utf-8', 
#df=pd.read_csv(file)
df=pd.read_csv('China_MatrixMap.csv',encoding='gb2312')
# 关闭文件

base_plot=(ggplot(df,aes(x='x',y='y'))+
geom_point(fill='w',colour="black",size=30)+ 
geom_text(aes(label='name'),size=12,family='SimHei')+
scale_y_reverse(limits =(8.5,0.5))+
scale_x_continuous(limits =(0.8,7.5))+
theme(
    axis_title=element_text(size=18,face="plain",color="black"),
    axis_text = element_text(size=15,face="plain",color="black"),
    figure_size = (7, 9),
    dpi = 50
))
print(base_plot)


base_plot=(ggplot(df,aes(x='x',y='y'))+
geom_tile(fill='w',colour="black",size=1)+ 
geom_text(aes(label='name'),size=12,family='SimHei')+
scale_y_reverse(limits =(8.5,0.5))+
scale_x_continuous(limits =(0.5,7.5),expand=(0.05,0.05))+
theme(
    axis_title=element_text(size=18,face="plain",color="black"),
    axis_text = element_text(size=15,face="plain",color="black"),
    figure_size = (9, 9),
    dpi = 50
))
print(base_plot)

#-----------------------------------------------------------------

df=pd.read_csv('China_MatrixMap.csv',encoding='gb2312')

ax = plt.figure(figsize=(6, 6)).gca()
patches = []
for x,y,name in zip(df['x'],df['y'],df['name']):
    rect = mpathes.Rectangle((x,-y),width=1, height=1)
    patches.append(rect)
    ax.text(x+0.5,-y+0.5,name,fontsize=12,verticalalignment="center",horizontalalignment="center")

collection = PatchCollection(patches, facecolor='w',edgecolor='k',linewidth=1)
ax.add_collection(collection)
plt.axis('equal')
plt.show()

# =============================================================================
# color_value =[x*y for x,y in zip(df['x'],df['y'])]
# collection = PatchCollection(patches, alpha=1,cmap=plt.cm.Spectral_r,edgecolor='k',linewidth=1)#facecolor='w',
# collection.set_array(np.array(color_value))
# ax.add_collection(collection)
# plt.axis('equal')
# plt.show()
# =============================================================================


ax = plt.figure(figsize=(6, 6)).gca()
patches = []
for x,y,name in zip(df['x'],df['y'],df['name']):
    rect = mpathes.Ellipse((x,-y),width=1, height=1)
    patches.append(rect)
    ax.text(x,-y,name,fontsize=12,verticalalignment="center",horizontalalignment="center")

collection = PatchCollection(patches, facecolor='w',edgecolor='k',linewidth=1)
ax.add_collection(collection)
plt.axis('equal')
plt.show()

# =============================================================================
# color_value =[x*y for x,y in zip(df['x'],df['y'])]
# collection = PatchCollection(patches, alpha=1,cmap=plt.cm.Spectral_r,edgecolor='k',linewidth=1)#facecolor='w',
# collection.set_array(np.array(color_value))
# ax.add_collection(collection)
# plt.axis('equal')
# plt.show()
# =============================================================================
