# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:33:54 2018
Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
@author: Jie Zhang
"""
from urllib.parse import quote  
from urllib import request  
import json  
import csv
import time
import re
import pandas as pd

amap_web_key = 'bc76d5878a6a96afb43beab66126ecc7'#'3e65b5abc153f1aac68ec95b3a468e76'   #
poi_search_url = "http://restapi.amap.com/v3/place/text"  
poi_boundary_url = "https://ditu.amap.com/detail/get/detail"  
import pandas as pd

#根据城市名称和分类关键字获取poi数据  
def getpois(cityname, keywords):      
    try:
        result = getpoi_page(cityname, keywords, 1)  
        result = json.loads(result)  # 将字符串转换为json  
        pois = result['pois']
        return pois[0] 
    except:
        return '未获取经纬度'
  
#将返回的poi数据装入集合返回  
def hand(poilist, result):  
    #result = json.loads(result)  # 将字符串转换为json  
    pois = result['pois']  
    for i in range(len(pois)) :  
        poilist.append(pois[i])  
        
#单页获取pois  
def getpoi_page(cityname, keywords, page):  
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&keywords=' + quote(keywords) + '&city=' + quote(cityname) + '&citylimit=true' + '&offset=25' + '&page=' + str(page) + '&output=json'  
    data = ''  
    with request.urlopen(req_url) as f:  
        data = f.read()  
        data = data.decode('utf-8')  
    return data 


#获取城市分类数据  

cityname = "深圳"  
Housename = "罗湖地铁站"  
pois = getpois(cityname,Housename)  
 
##
total=[]    
Station_info={}             #新建一个字典用于存放单个房屋的信息
Station_info['Station_Title']='Station_Title'
Station_info['Subway_Num2']='Subway_Num2'
Station_info['Station2']='Station2'
Station_info['longitude']='longitude'
Station_info['latitude']='latitude'
total.append(Station_info)
i=0
with open('ShenzhenSubway_Station_WithXY.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        i=i+1
        if (i<1000):
            pois = getpois(cityname, row['Station']) 
            if (pois=='未获取经纬度'):
                continue
            Station_info={}             #新建一个字典用于存放单个房屋的信息
            Station_info['Station_Title']=row['Station_Title']
            Station_info['Station2']=pois['name']
            Station_info['Subway_Num2']=pois['address']
            Station_info['latitude']=pois['location'].split(",")[0]
            Station_info['longitude']=pois['location'].split(",")[1]
            total.append(Station_info) 
   
my_df_Location = pd.DataFrame(total)
file=open('ShenzhenSubway_Station_WithXY.csv')
my_df_XY=pd.read_csv(file)
my_df=pd.merge(my_df_Location,my_df_XY,on='Station_Title')
#my_df.to_csv('ShenzhenSubway_Station_WithLocation.csv', index=False, header=False)
        


