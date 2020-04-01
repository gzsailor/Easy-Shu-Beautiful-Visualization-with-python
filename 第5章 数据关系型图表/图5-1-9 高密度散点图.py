# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:48:44 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
from plotnine import *
from sklearn.cluster import KMeans

df=pd.read_csv('HighDensity_Scatter_Data.csv')

#--------------------------------------(b) 带透明度设置的散点图------------------------------------
base_plot1=(ggplot(df, aes('x','y')) +
  geom_point( colour="black",alpha=0.1)+
  labs(x = "Axis X",y="Axis Y")+
 theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1,
       figure_size = (5, 5),
       dpi = 100
       )
)
print(base_plot1)

#------------------------------------- (d) 带椭圆标定的聚类散点图-------------------------
estimator = KMeans(n_clusters=2)#构造聚类器
estimator.fit(df)#聚类
df['label_pred'] = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和


# mydata为x和y两列数据组成，kmeans聚类算法
#将分类结果转变成类别变量(categorical variables)
base_plot2=(ggplot(df, aes('x','y',color='factor(label_pred)')) +
   geom_point (alpha=0.2)+
  # 绘制透明度为0.2 的散点图
  stat_ellipse(aes(x='x',y='y',fill= 'factor(label_pred)'), geom="polygon", level=0.95, alpha=0.2) +
  #绘制椭圆标定不同类别，如果省略该语句，则绘制图3-1-7(c)
  scale_color_manual(values=("#00AFBB","#FC4E07")) +#使用不同颜色标定不同数据类别
  scale_fill_manual(values=("#00AFBB","#FC4E07"))+  #使用不同颜色标定不同椭类别
  theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1,
       figure_size = (5,5),
       dpi = 100
       )
)
print(base_plot2)