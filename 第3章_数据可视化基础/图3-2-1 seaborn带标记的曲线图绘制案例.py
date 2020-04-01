# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:11:34 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#from matplotlib import cm#,colors
import seaborn as sns


import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号

df=pd.read_csv("MappingAnalysis_Data.csv")

sns.set_palette("Set1")
sns.set_style("ticks")
sns.set_context( rc={'axes.labelsize': 15, 'legend.fontsize':13, 
                    'xtick.labelsize': 13,'ytick.labelsize': 13})

#-------------------------------------(a)--------------------------------------------
fig = plt.figure(figsize=(5,4), dpi=100)

sns_line=sns.lineplot(x="Time", y="value",
                  hue="variable", style="variable",data=df,
                  markers=True, dashes=False)
#fig.savefig("seaborn1.pdf")
#-----------------------------------(b)-----------------------------------------------
markers=['o','s','H','D']    
#colors=['#e41a1c','#377eb8','#4daf4a','#984ea3']
fig = plt.figure(figsize=(5,4), dpi=100)

sns_line=sns.lineplot(x="Time", y="value",
                  hue="variable",style="variable",data=df,
                  markers=markers,dashes=False,
                  markersize=8,markeredgewidth=0.5,markeredgecolor="k",
                  linewidth=1)

#plt.legend(loc='upper left',edgecolor='none',facecolor='none')


#fig.savefig("seaborn2.pdf")
#----------------------------------(c)--------------------------------------------------
markers=['o','s','H','D']    
#colors=['#e41a1c','#377eb8','#4daf4a','#984ea3']
fig = plt.figure(figsize=(5,4), dpi=100)

sns_line=sns.lineplot(x="Time", y="value",
                  hue="variable",style="variable",data=df,
                  markers=markers,dashes=False,
                  markersize=8,markeredgewidth=0.5,markeredgecolor="k",
                  linewidth=1)

#
plt.xlabel("Time(d)")
plt.ylabel("value")

plt.xlim(-1,20)
plt.ylim(-2,90)
# 设置横轴记号
plt.xticks(np.linspace(0,20,11,endpoint=True))
# 设置纵轴的上下限
plt.yticks(np.linspace(0,90,10,endpoint=True))

plt.legend(loc='upper left',edgecolor='none',facecolor='none')
#ax = plt.gca()
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles=handles[1:], labels=labels[1:],loc='upper left',edgecolor='none',facecolor='none')

plt.show()

#fig.savefig("seaborn3.pdf")
#--------------------------------------(d)------------------------------------------
sns.set_style("ticks")
#sns.sinplot() # 默认无参数状态，就是删除上方和右方的边框
#sns.despine()
#sns.despine()

markers=['o','s','H','D']    
#colors=['#e41a1c','#377eb8','#4daf4a','#984ea3']
fig = plt.figure(figsize=(5,4), dpi=100)

sns_line=sns.lineplot(x="Time", y="value",
                  hue="variable",style="variable",data=df,
                  markers=markers,dashes=False,
                  markersize=8,markeredgewidth=0.5,markeredgecolor="k",
                  linewidth=1)

#plt.legend(loc='upper left',edgecolor='none',facecolor='none')

plt.xlabel("Time(d)")
plt.ylabel("value")

plt.xlim(-1,20)
plt.ylim(-2,90)
# 设置横轴记号
plt.xticks(np.linspace(0,20,11,endpoint=True))
# 设置纵轴的上下限
plt.yticks(np.linspace(0,90,10,endpoint=True))

sns.despine()
ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[1:], labels=labels[1:],loc='upper left',edgecolor='none',facecolor='none')

plt.show()

#fig.savefig("seaborn4.pdf")
