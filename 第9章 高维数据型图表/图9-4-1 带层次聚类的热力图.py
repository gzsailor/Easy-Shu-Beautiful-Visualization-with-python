# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:35 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from plotnine.data import mtcars
from sklearn.preprocessing import scale

sns.set_style("white")
sns.set_context("notebook", font_scale=1.5,
                rc={'axes.labelsize': 17, 'legend.fontsize':17, 
                    'xtick.labelsize': 15,'ytick.labelsize': 10})

df=mtcars.set_index('name')
df.loc[:,:] = scale(df.values )

#------------------------------- (a)热力图------------------------------------------------------
fig=plt.figure(figsize=(7, 7),dpi=80)
sns.heatmap(df, center=0, cmap="RdYlBu_r",
               linewidths=.15,linecolor='k')
#sns.set()
plt.savefig('heatmap2.pdf')

#--------------------------------(b)带层次聚类的热力图.-----------------------------------------------------------
sns.clustermap(df, center=0, cmap="RdYlBu_r",
               linewidths=.15,linecolor='k', figsize=(8, 8))
#plt.savefig('heatmap1.pdf')



#----------------------------------------案例------------------------------------------------------
# Load the brain networks example dataset
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

# Select a subset of the networks
used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
used_columns = (df.columns.get_level_values("network")
                          .astype(int)
                          .isin(used_networks))
df = df.loc[:, used_columns]

# Create a categorical palette to identify the networks
network_pal = sns.husl_palette(8, s=.45)
network_lut = dict(zip(map(str, used_networks), network_pal))

# Convert the palette to vectors that will be drawn on the side of the matrix
networks = df.columns.get_level_values("network")
network_colors = pd.Series(networks, index=df.columns).map(network_lut)

# Draw the full plot
sns.clustermap(df.corr(), center=0, cmap="vlag",
               row_colors=network_colors, col_colors=network_colors,
               linewidths=.75, figsize=(7, 7))

