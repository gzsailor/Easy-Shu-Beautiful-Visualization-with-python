# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:45:50 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import numpy as np
from matplotlib import cm#,colors
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure, show, rc

#import matplotlib.dates as mdates
import pandas as pd
#from datetime import datetime
import matplotlib as mpl
plt.rcParams["patch.force_edgecolor"] = True

#years = mdates.YearLocator()   # every year
#months = mdates.MonthLocator()  # every month
#monthsFmt = mdates.DateFormatter('%M')

df=pd.read_csv('PloarRange_Data.csv')

fig = figure(figsize=(5,5),dpi =90)    
ax = fig.add_axes([0.1, 0.1, 0.6, 0.6], polar=True)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_rlabel_position(0)

plt.xticks(np.arange(0,359,30)/180*np.pi,["%.2d" % i for i in np.arange(1,13,1)], color="black", size=12)
plt.ylim(-10,35)
plt.yticks(np.arange(-10,40,10),color="black", size=12,verticalalignment='center',horizontalalignment='right')

plt.grid(which='major',axis ="x", linestyle='-', linewidth='0.5', color='gray',alpha=0.5)
plt.grid(which='major',axis ="y", linestyle='-', linewidth='0.5', color='gray',alpha=0.5)

N = df.shape[0]

x_angles = [n / float(N) * 2 * np.pi for n in range(N)]
#x_angles += x_angles[:1]


upperlimits =(df['max.temperaturec']-df['min.temperaturec']).values
#upperlimits += upperlimits[:1]
lowerlimits = df['min.temperaturec'].values
#lowerlimits += lowerlimits[:1]

colors = cm.Spectral_r(upperlimits / float(max(upperlimits)))

#ax.bar(x_angles,lowerlimits, color='none',edgecolor='none',width=0.01,alpha=1)
#ax.bar(x_angles,upperlimits, color=colors,edgecolor='none',width=0.02, bottom=lowerlimits,alpha=1)

ax.bar(x_angles,lowerlimits, color='none',edgecolor='none',width=0.01,alpha=1)
ax.bar(x_angles,upperlimits, color=colors,edgecolor='none',width=0.02, bottom=lowerlimits,alpha=1)

ax2 = fig.add_axes([0.8, 0.25, 0.05, 0.3])
cmap = mpl.cm.Spectral_r
norm = mpl.colors.Normalize(vmin=0, vmax=20)
bounds = np.arange(0,20,0.1)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,norm=norm,boundaries=bounds,ticks=np.arange(0,20,5),spacing='proportional',label='Temperature')

plt.show()

#fig.savefig("图3-7-3极坐标跨度图_1.pdf")

