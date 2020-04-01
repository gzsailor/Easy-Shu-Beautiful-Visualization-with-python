# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:15:14 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

from statsmodels.formula.api import ols
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Surface_Data.csv')
##多项式拟合z=f(x, y)=a+bx+cy+dx2+ey2

formula = 'z~x+np.square(x)+y+np.square(y)'
est = ols(formula,data=df).fit()
print(est.summary())

N=30
xmar= np.linspace(min(df.x),max(df.x),N)
ymar= np.linspace(min(df.y),max(df.y),N)
X,Y=np.meshgrid(xmar,ymar)
df_grid =pd.DataFrame({'x':X.flatten(),'y':Y.flatten()})

Z=est.predict(df_grid)

fig = plt.figure(figsize=(10,8),dpi =90)  
ax = fig.gca(projection='3d')
#ax =  fig.add_subplot(projection='3d')
#ax.set_aspect('equal','box')
ax.view_init(azim=60, elev=20)
##改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴

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

p=ax.plot_surface(X,Y, Z.values.reshape(N,N), rstride=1, cstride=1, cmap='Spectral_r',
                  alpha=1,edgecolor='k',linewidth=0.25)

ax.set_xlabel( "Gax Mileage (mpg)")
ax.set_ylabel("0-60 mph (sec)")
ax.set_zlabel("Power (KW)")
ax.set_zlim(50,170)


cbar=fig.colorbar(p, shrink=0.5,aspect=10)
cbar.set_label('Power (kW)')
#fig.savefig('三维曲面图2.pdf')


#-------------------------等高线图---------------------------------------------------

fig, ax = plt.subplots(figsize=(5,4),dpi =90)  

CS=ax.contour(X,Y, Z.values.reshape(N,N), levels=10, linewidths=0.5, colors='k')
cntr = ax.contourf(X,Y, Z.values.reshape(N,N), levels=10, cmap="Spectral_r")
#scat=ax.scatter(df.x, df.y,c=df.z,s=40, linewidths=0.5, edgecolors="k",alpha=0.8)
ax.set_xlabel( "Gax Mileage (mpg)")
ax.set_ylabel("0-60 mph (sec)")

fig.colorbar(cntr,ax=ax,label="Power (KW)")                
CS.levels = [int(val) for val in cntr.levels]
ax.clabel(CS, CS.levels, fmt='%.0f', inline=True,  fontsize=10)
