# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:49:42 2018
Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
@author: Peter_Zhang
"""
import csv
import pandas as pd
import numpy as np


pi=3.1415926
House_Price=[]
with open('ShenzhenHousing_Price_WithLocation.csv.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
         info={}             #新建一个字典用于存放单个房屋的信息
         info={'latitude':row['longitude'],
          'longitude':row['latitude'],
          'unit_price':row['unit_price']}
         House_Price.append(info)
                 
Train_info=[]
with open('ShenzhenSubway_Station_WithLocation.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
         info={}             #新建一个字典用于存放单个房屋的信息  
         info={'Station_Title':row['Station_Title'],
               'latitude':row['latitude'],
               'longitude':row['longitude'],
                'y':row['y'],
               'x':row['x'],
               'Subway_Num2':row['Subway_Num2'],
          }
         Train_info.append(info)
         
N_House=len(House_Price)
N_Train=len(Train_info)  
Thresold_D=3

#http://blog.csdn.net/koryako/article/details/51864161
#设第一点A的经 纬度为(LonA, LatA)，第二点B的经纬度为(LonB, LatB)，
#按照0度经线的基准，东经取经度的正值(Longitude)，西经取经度负值(-Longitude)，北纬取90-纬度值(90- Latitude)，南纬取90+纬度值(90+Latitude)，
#则经过上述处理过后的两点被计为(MLonA, MLatA)和(MLonB, MLatB)。那么根据三角推导，可以得到计算两点距离的如下公式：
#C = sin(MLatA)*sin(MLatB)*cos(MLonA-MLonB) + cos(MLatA)*cos(MLatB)
#Distance = R*Arccos(C)*Pi/180
#如果仅对经度作正负的处理，而不对纬度作90-Latitude(假设都是北半球，南半球只有澳洲具有应用意义)的处理，那么公式将是：
#C = sin(LatA)*sin(LatB) + cos(LatA)*cos(LatB)*cos(MLonA-MLonB)
#Distance = R*Arccos(C)*Pi/180
Train_price=[]
for i in range(0,N_Train):
    Stat_x=float(Train_info[i]['latitude'])
    Stat_y=float(Train_info[i]['longitude'])
    Neighbor=[]
    for j in range(0,N_House):
        House_x=float(House_Price[j]['latitude'])
        House_y=float(House_Price[j]['longitude'])
        D=np.arccos((np.sin(Stat_x*pi/180)*np.sin(House_x*pi/180))+(np.cos(Stat_x*pi/180)*np.cos(House_x*pi/180)*np.cos(Stat_y-House_y)))*6371.004*pi/180
        #print(D)
        if (D<=Thresold_D):
            Neighbor.append(float(House_Price[j]['unit_price']))
    print(np.mean(Neighbor))
    Train_price.append(np.mean(Neighbor))
        
 
my_df = pd.DataFrame(Train_price)
#my_df.to_csv('ShenzhenSubway_StationHousingPrice.csv', index=False, header=False)        
         
         