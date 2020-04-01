# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:49 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_style("darkgrid",{'axes.facecolor': '.95'})
sns.set_context("notebook", font_scale=1.5,
                rc={'axes.labelsize': 13, 'legend.fontsize':13, 
                    'xtick.labelsize': 12,'ytick.labelsize': 12})

df = sns.load_dataset("iris")

#------------------------------------(a) 单数据系列-------------------------------------------------

g=sns.pairplot(df, height =2)

g = g.map_diag(plt.hist,color='#00C07C',density=False,edgecolor="k",bins=10,alpha=0.8,linewidth=0.5)
g = g.map_offdiag(plt.scatter, color='#00C2C2',edgecolor="k", s=30,linewidth=0.25)

plt.subplots_adjust(hspace=0.05, wspace=0.05)
#g.savefig('Matrix_Scatter2.pdf')

#--------------------------------(b) 多数据系列------------------------------------------------------
g=sns.pairplot(df, hue="species",height =2,palette ='Set1')

g = g.map_diag(sns.kdeplot, lw=1, legend=False)

g = g.map_offdiag(plt.scatter, edgecolor="k", s=30,linewidth=0.2)


plt.subplots_adjust(hspace=0.05, wspace=0.05)

#g.savefig('Matrix_Scatter1.pdf')
