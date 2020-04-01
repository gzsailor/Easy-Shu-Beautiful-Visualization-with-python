# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:56:15 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import numpy as np
from matplotlib import cm,colors
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure, show, rc
import pandas as pd

plt.rcParams["patch.force_edgecolor"] = True
   
mydata=pd.DataFrame(dict(day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
                      Peter=[10, 60, 50, 20,10,90,30],
                      Jack=[20,50, 10, 10,30,60,50],
                      Eelin=[30, 50, 20, 40,10,40,50]))

n_row = mydata.shape[0]
n_col= mydata.shape[1]
angle = np.arange(0,2*np.pi,2*np.pi/n_row)
    #绘制的数据
    
cmap=cm.get_cmap('Reds',n_col)
color=[colors.rgb2hex(cmap(i)[:3]) for i in range(cmap.N) ]
    
radius1 = np.array(mydata.Peter)
radius2 = np.array(mydata.Jack)
radius3 = np.array(mydata.Eelin)

fig = figure(figsize=(4,4),dpi =90)    
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

#方法用于设置角度偏离,参数值为弧度值数值
ax.set_theta_offset(np.pi/2)
#当set_theta_direction的参数值为1,'counterclockwise'或者是'anticlockwise'的时候，正方向为逆时针；
#当set_theta_direction的参数值为-1或者是'clockwise'的时候，正方向为顺时针；
ax.set_theta_direction(-1)
#方法用于设置极径标签显示位置,参数为标签所要显示在的角度
ax.set_rlabel_position(360)


barwidth1=0.2  
barwidth2=0.2
plt.bar(angle,radius1,width=barwidth2, align="center",color=color[0],edgecolor="k",alpha=1,label="Peter")
plt.bar(angle+barwidth1,radius2,width=barwidth2,align="center", color=color[1],edgecolor="k",alpha=1,label="Jack")
plt.bar(angle+barwidth1*2,radius3,width=barwidth2,align="center", color=color[2],edgecolor="k",alpha=1,label="Eelin")

plt.legend(loc="center",bbox_to_anchor=(1.2, 0, 0, 1))

plt.ylim(-30,100)
plt.xticks(angle+2*np.pi/n_row/4,labels=mydata.day,size=12)

plt.yticks(np.arange(0,101,30),verticalalignment='center',horizontalalignment='right')


plt.grid(which='major',axis ="x", linestyle='-', linewidth='0.5', color='gray',alpha=0.5)
plt.grid(which='major',axis ="y", linestyle='-', linewidth='0.5', color='gray',alpha=0.5)

#fig.savefig('径向柱图2.pdf')


