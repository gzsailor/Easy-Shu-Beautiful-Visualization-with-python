# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:56:27 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"]='Arial'   
#plt.rcParams["font.sans-serif"]='SimHei' #汉字显示设定
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['axes.facecolor']='#CFDBE7'
plt.rcParams['savefig.facecolor'] ='#CFDBE7'
plt.rc('axes',axisbelow=True)    #使网格线置于图表下层

df=pd.read_excel(r"多数据系列柱形图.xlsx",sheet_name="原始数据")
df=df.sort_values("INFO-Processing",ascending=False)  #降序处理


x_lable=np.array(df["Quarter"])
x=np.arange(len(x_lable))
y1=np.array(df["INFO-Processing"])
y2=np.array(df["TOTAL"])
width=0.35
fig=plt.figure(figsize=(5,4.5),dpi=100,facecolor='#CFDBE7') 

plt.bar(x,y1,width=width,color='#01516C',label='INFO-Processing')  #调整y1轴位置，颜色，label为图例名称，与下方legend结合使用
plt.bar(x+width,y2,width=width,color='#01A4DC',label='TOTAL')       #调整y2轴位置，颜色，label为图例名称，与下方legend结合使用
plt.xticks(x+width/2,x_lable,size=12)      #设置x轴刻度，位置,大小
plt.yticks(size=12)                        #设置y轴刻度，位置,大小
plt.grid(axis="y",c='w',linewidth=1.2)     #设置y轴网格线的颜色与粗细
                     #将y轴网格线置于底层
#plt.xlabel("Quarter",labelpad=10,size=18,)                          #设置x轴标签,labelpad设置标签距离x轴的位置
#plt.ylabel("Amount",labelpad=10,size=18,)                           #设置y轴标签,labelpad设置标签距离y轴的位置

#显示图例，loc图例显示位置(可以用坐标方法显示），ncol图例显示几列，默认为1列,frameon设置图形边框
plt.legend(loc=(0,1.02),ncol=2,frameon=False)  
 
ax = plt.gca()                        #获取整个绘图区的句柄
ax.spines['top'].set_color('none')    #设置上‘脊梁’为无色
ax.spines['right'].set_color('none')  #设置右‘脊梁’为无色
ax.spines['left'].set_color('none')   #设置左‘脊梁’为无色
ax.yaxis.set_ticks_position('right')  #y轴放置在y右边

#添加主标题
plt.text(0.,1.25,s='WHERE CAPITAL SPENDING\nIS STILL HOT',transform=ax.transAxes,weight='bold',size=20)    
#添加副标题
plt.text(0,1.12,s='Column charts are used to compare values\nacross categories by using vertical bars.',transform=ax.transAxes,
         weight='light',size=15)   
#添加脚注
plt.text(0.,-0.15,s='Sources: http://zhuanlan.zhihu.com/apeter-zhang-jie',transform=ax.transAxes,weight='light',size=10)     

#plt.savefig('商业图表_经济学人1.pdf',bbox_inches='tight', pad_inches=0.3)
plt.show()   