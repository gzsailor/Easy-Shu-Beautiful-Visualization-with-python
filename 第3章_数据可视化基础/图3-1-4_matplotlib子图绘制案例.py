# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:53:54 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.style.use('default') #print(plt.style.available)


df=pd.read_csv("MappingAnalysis_Data.csv")

df1=df[df.variable=='0%(Control)']
df2=df[df.variable=='1%']
df3=df[df.variable=='5%']
df4=df[df.variable=='15%']

# =============================================================================
colors=['#e41a1c','#377eb8','#4daf4a','#984ea3']
markers=['o','s','H','D']    
labels=["0%(Control)","1%","5%","15%"]
group=["0%(Control)","1%","5%","15%"]#np.unique(df.variable)

#---------------------------------------------------------------------------
fig,(ax0,ax1)= plt.subplots(nrows=1,ncols=2,sharey=True,figsize=(8,3))

ax0.plot(df1.Time, df1.value, 
         marker=markers[0], markerfacecolor=colors[0], markersize=8,markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-",label=labels[0])
ax0.plot(df2.Time, df2.value, 
         marker=markers[1], markerfacecolor=colors[1], markersize=7,markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-",label=labels[1])
ax0.spines['right'].set_color('none')
ax0.spines['top'].set_color('none')
#ax0.set_xlabel("Time(d)",fontsize=14)
#ax0.set_ylabel("value",fontsize=14)
ax0.set_xlabel("Time(d)",fontsize=14)
ax0.set_ylabel("value",fontsize=14)

ax0.set_xlim(-1,20)
ax0.set_ylim(-2,90)
# 设置横轴记号
ax0.set_xticks(np.linspace(0,20,11,endpoint=True))
# 设置纵轴的上下限
ax0.set_yticks(np.linspace(0,90,10,endpoint=True))

ax0.legend(loc='upper left',edgecolor='none',facecolor='none')


ax1.plot(df1.Time, df1.value, 
         marker=markers[0], markerfacecolor=colors[0], markersize=8,markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-",label=labels[0])
ax1.plot(df3.Time, df3.value, 
         marker=markers[2], markerfacecolor=colors[2], markersize=8,markeredgewidth=0.5,
         color="k", linewidth=0.5, linestyle="-",label=labels[2])
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax1.set_xlabel("Time(d)",fontsize=14)
#ax1.set_ylabel("value",fontsize=14)

ax1.set_xlim(-1,20)
ax1.set_ylim(-2,90)
# 设置横轴记号
ax1.set_xticks(np.linspace(0,20,11,endpoint=True))
# 设置纵轴的上下限
ax1.set_yticks(np.linspace(0,90,10,endpoint=True))

ax1.legend(loc='upper left',edgecolor='none',facecolor='none')
#plt.xlabel("Time(d)",fontsize=14)
#plt.ylabel("value",fontsize=14)
#fig.savefig("matplotlib5.pdf")