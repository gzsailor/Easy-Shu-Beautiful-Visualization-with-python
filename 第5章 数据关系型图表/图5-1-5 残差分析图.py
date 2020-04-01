# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:28:18 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
import statsmodels.api as sm

df=pd.read_csv('Residual_Analysis_Data.csv')

#-----------------------------------(a) 线性回归----------------------------------------
results = sm.OLS(df.y2, df.x).fit()

df['predicted']=results.predict()   # 保存预测值
df['residuals']=df.predicted-df.y2   #保存残差(有正有负)
df['Abs_Residuals']=np.abs(df.residuals)  #保存残差的绝对值
#mydata包含x、y2、predicted、residuals、Abs_Residuals 共5列数值
base_Residuals=(ggplot(df, aes(x = 'x', y = 'y2')) +
  geom_point(aes(fill ='Abs_Residuals', size = 'Abs_Residuals'),shape='o',colour="black") +
# 使用实际值绘制气泡图，并将气泡的颜色和面积映射到残差的绝对值Abs_Residuals
  geom_line(aes(y = 'predicted'), color = "lightgrey") + #添加空心圆圈的预测值
  geom_point(aes(y = 'predicted'), shape = 'o') + #添加空心圆圈的预测值
  geom_segment(aes(xend = 'x', yend = 'predicted'), alpha = .2) +#添加实际值和预测值的连接线...
  
  scale_fill_gradientn(colors = ["black", "red"]) + #填充颜色映射到red单色渐变系
  
  guides(fill = guide_legend(title="Rresidual"),
         size = guide_legend(title="Rresidual"))+      
  theme(
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       #legend_position="none",
       aspect_ratio =1.1,
       figure_size = (5, 5),
       dpi = 100)
)
print(base_Residuals)

#---------------------------------------(b)二次回归------------------------------------------
X = np.column_stack((df.x, df.x**2))
#使用 sm.add_constant() 在 array 上加入一列常项 1。
X = sm.add_constant(X)
results = sm.OLS(df.y5, X).fit()

df['predicted']=results.predict()   # 保存预测值
df['residuals']=df.predicted-df.y5   #保存残差(有正有负)
df['Abs_Residuals']=np.abs(df.residuals)  #保存残差的绝对值
#mydata包含x、y2、predicted、residuals、Abs_Residuals 共5列数值
base_Residuals=(ggplot(df, aes(x = 'x', y = 'y5')) +
  geom_point(aes(fill ='Abs_Residuals', size = 'Abs_Residuals'),shape='o',colour="black") +
# 使用实际值绘制气泡图，并将气泡的颜色和面积映射到残差的绝对值Abs_Residuals
  #geom_smooth(method = "lm", se = False, color = "lightgrey") + # 添加灰色的线性拟合曲线
  geom_line(aes(y = 'predicted'), color = "lightgrey") + #添加空心圆圈的预测值
  geom_point(aes(y = 'predicted'), shape = 'o') + #添加空心圆圈的预测值
  geom_segment(aes(xend = 'x', yend = 'predicted'), alpha = .2) +#添加实际值和预测值的连接线...
  
  scale_fill_gradientn(colors = ["black", "red"]) + #填充颜色映射到red单色渐变系
  
  guides(fill = guide_legend(title="Rresidual"),
         size = guide_legend(title="Rresidual"))+      
  theme(
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       #legend_position="none",
       aspect_ratio =1.1,
       figure_size = (5, 5),
       dpi = 100)
)
print(base_Residuals)