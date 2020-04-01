# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:26:53 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

N=5000
x1 = np.random.normal(1.5,1, N)
y1 =np.random.normal(1.6,1, N)
x2 = np.random.normal(2.5,1, N)
y2 =np.random.normal(2.2,1, N)

df=pd.DataFrame({'x':np.append(x1,x2),'y':np.append(y1,y2)})

#-------------------------------------(a) 方块形.------------------------------------------
bin_plot=(ggplot(df, aes('x','y')) 
+stat_bin2d(bins=40) 
+scale_fill_cmap(name ='Spectral_r')
+theme_matplotlib()
+theme(#legend_position='none',
       text=element_text(size=12,colour = "black"),
       aspect_ratio =1,
       dpi=100,
       figure_size=(4,4)))
print(bin_plot)

#bin_plot.save("bin_plot.pdf") 
#-------------------------------------(a) 方块形.------------------------------------------
fig = plt.figure(figsize=[3,2.7],dpi=130)
h=plt.hist2d(df['x'], df['y'], bins=40,cmap=plt.cm.Spectral_r,cmin =1)
ax=plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')
cbar=plt.colorbar(h[3])
cbar.set_label('count')
cbar.set_ticks(np.linspace(0,60,7))
plt.show()
#fig.savefig('bin_plot2.pdf')

#-------------------------------------(b)六方形.------------------------------------------
fig, ax = plt.subplots(figsize=[3,2.7],dpi=130)#
im = ax.hexbin(df['x'], df['y'],cmap=plt.cm.Spectral_r,gridsize=(20,20),mincnt=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
#ax.set_yticlabels()
cbar=fig.colorbar(im, ax=ax)
cbar.set_label('count')
#fig.savefig('hexbin_plot.pdf')


