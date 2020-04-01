# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:57:12 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
from sklearn import manifold, datasets

#------------------------------------(a) 四维数据的iris数据集----------------------------------------------------------
iris = datasets.load_iris()

tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(iris.data)
target=pd.Categorical.from_codes(iris.target,iris.target_names)
df=pd.DataFrame(dict(DistributedY1=X_tsne[:, 0],DistributedY2=X_tsne[:, 1],target=target))

base_plot2=(ggplot(df, aes('DistributedY1','DistributedY2',fill='target')) +
   geom_point (alpha=1,size=3,shape='o',colour='k')+
  # 绘制透明度为0.2 的散点图
 # stat_ellipse( geom="polygon", level=0.95, alpha=0.2) +
  #绘制椭圆标定不同类别，如果省略该语句，则绘制图3-1-7(c)
  #scale_color_manual(values=("#00AFBB","#FC4E07")) +#使用不同颜色标定不同数据类别
  scale_fill_manual(values=("#00AFBB", "#E7B800", "#FC4E07"),name='group')+  #使用不同颜色标定不同椭类别
  theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=13,face="plain",color="black"),
       axis_text = element_text(size=12,face="plain",color="black"),
       legend_text = element_text(size=11,face="plain",color="black"),
       legend_background=element_blank(),
       legend_position=(0.3,0.25),
       aspect_ratio =1,
       figure_size = (5,5),
       dpi = 100
       )
)
print(base_plot2)

#----------------------------------------(b) 93维数据的train数据集--------------------------------------------------
df=pd.read_csv('Tsne_Data.csv')
df=df.set_index('id')

num_rows_sample=5000

df = df.sample(n=num_rows_sample)

tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(df.iloc[:,:-1])

df=pd.DataFrame(dict(DistributedY1=X_tsne[:, 0],DistributedY2=X_tsne[:, 1],target=df.iloc[:,-1]))

base_plot2=(ggplot(df, aes('DistributedY1','DistributedY2',fill='target')) +
   geom_point (alpha=1,size=2,shape='o',colour='k',stroke=0.1)+
  # 绘制透明度为0.2 的散点图
 # stat_ellipse( geom="polygon", level=0.95, alpha=0.2) +
  #绘制椭圆标定不同类别，如果省略该语句，则绘制图3-1-7(c)
  #scale_color_manual(values=("#00AFBB","#FC4E07")) +#使用不同颜色标定不同数据类别
 # scale_fill_cmap(name ='Set1')+
  scale_fill_hue(s = 0.99, l = 0.65, h=0.0417,color_space='husl')+
  xlim(-100,100)+
  theme(
       #text=element_text(size=15,face="plain",color="black"),
        axis_title=element_text(size=13,face="plain",color="black"),
       axis_text = element_text(size=12,face="plain",color="black"),
       legend_text = element_text(size=11,face="plain",color="black"),
       aspect_ratio =1,
       figure_size = (5,5),
       dpi = 100
       )
)
print(base_plot2)