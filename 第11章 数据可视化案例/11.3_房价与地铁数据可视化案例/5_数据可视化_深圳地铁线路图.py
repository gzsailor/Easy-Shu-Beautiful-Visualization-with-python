# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:11:20 2018
Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
@author: Jie Zhang
"""

import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *

file = open('ShenzhenSubway_StationHousingPrice.csv')
mydata_station=pd.read_csv(file)

file = open('ShenzhenSubway_Path.csv')
mydata_Path=pd.read_csv(file)

mydata_Path['Subway_Num']=pd.Categorical(mydata_Path['Subway_Num'])
mydata_station['Subway_Num']=pd.Categorical(mydata_station['Subway_Num'])

#------------------------------------图11-3-3. 深圳市示意地铁线路图.----------------------------------------------
base_plot=(ggplot()+
  geom_path (mydata_Path,aes(x='x',y='y',group='Subway_Num',colour='Subway_Num'), size=1)+
  geom_point(mydata_station,aes(x='x',y='y',group='Subway_Num',colour='Subway_Num'),shape='o',size=3,fill="white")+
  xlab("long")+
  ylab("lat"))

print(base_plot)


#----------------------------------图11-3-9. 深圳市地铁线路房价分布图.----------------------------------------------
Price_max=np.max(mydata_station['Unit_Price']) # 89503.92558
Price_min=np.min(mydata_station['Unit_Price'])

mydata_station['Unit_Price2']=pd.cut(mydata_station['Unit_Price'],
              bins=[0,30000,40000,50000,60000,70000,80000,90000],
              labels=[" <=30000","30000~40000","40000~50000","50000~60000","60000~70000","70000~80000","80000~90000"])

base_plot=(ggplot()+
  geom_path (mydata_Path,aes(x='x',y='y',group='Subway_Num',colour='Subway_Num'), size=1)+
  geom_point(mydata_station,aes(x='x',y='y',group='Subway_Num2',size='Unit_Price2',fill='Unit_Price2'),shape='o')+
  #guides(fill = guide_legend((title="二手房均价(平方米)")),
  #       size = guide_legend((title="二手房均价(平方米)")))+
  theme_void()+
  theme(
    figure_size = (11, 11),
    dpi = 58
))
print(base_plot)

#-------------------------------------图11-3-8. 楼盘分布散点地图.--------------------------------------------------
file = open('ShenzhenHousing_Price_WithLocation.csv')
mydata_house=pd.read_csv(file)
file.close()
base_plot=(ggplot()+
  geom_point(mydata_house,aes(x='longitude',y='latitude',fill='unit_price'),shape='o',size=1,alpha=0.8,color='none')+
  geom_path (mydata_station,aes(x='long',y='lat',group='Subway_Num'), size=0.5,linejoin = "bevel", lineend = "square")+
  geom_point(mydata_station,aes(x='long',y='lat'),shape='o',size=2,fill="white",color='black',stroke=0.1)+
  scale_fill_cmap(name = 'RdYlGn')+
  xlab("long")+
  ylab("lat"))
print(base_plot)
