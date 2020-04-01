# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:01:42 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import matplotlib.pyplot as plt     
import numpy as np
import pandas as pd

df=pd.DataFrame(dict(group=["Manufacturing","Transportationm warehousing","Education services, healt care,social assistance",
                            "Construction","Information","Retail trade","Professional and business services",
                            "Finance, insurace,real estate, rental, leasing"],
                      price=[1.08,0.74,0.73,0.66,0.55,0.54,0.356,0.28]))

df=df.sort_values(by=["price"],ascending=True)
x_label=np.array(df['group'])
y=np.array(df['price'])
x_value=np.arange(len(x_label))
height=0.45

fig=plt.figure(figsize=(5,5))
plt.xticks([])
plt.yticks([])
ax = plt.gca()                     #获取整个表格边框
ax.spines['top'].set_color('none')     #设置上‘脊梁’为无色
ax.spines['right'].set_color('none')     #设置右‘脊梁’为无色
ax.spines['left'].set_color('none')      #设置左‘脊梁’为无色
ax.spines['bottom'].set_color('none')  #设置下‘脊梁’为无色
plt.barh(x_value,color='#0099DC',height=height,width=y,align="center")
for a,b,label in zip(y,x_value,x_label):    #给条形图加标签，需要使用for循环
    plt.text(0, b+0.45, s=label, ha='left', va= 'center',fontsize=13,family='sans-serif')
    plt.text(a+0.01, b, s="$"+ str(round(a,2)), ha='left', va= 'center',fontsize=13.5,family='Arial',weight="bold")

plt.text(0,1.3,s='Economic Engine',transform=ax.transAxes,weight='bold',size=20,family='Arial')
plt.text(0,1.05,s="Manufacturing has a big impact on the U.S.\neconomy's health. Everay dollar of value added\nin these areas generates the following amounts\nof additional transsactions: ",
               transform=ax.transAxes,weight='light',size=14,family='sans-serif')
plt.text(0,-0.05,s='Source: Daniel J. Meckstroth.MAPI Foundtation;U.S. Bureau\nof Economic Analysis',transform=ax.transAxes,weight='light',size=10,family='sans-serif')
#plt.savefig('商业图表_条形图.pdf',bbox_inches='tight', pad_inches=0.3)
plt.show()
