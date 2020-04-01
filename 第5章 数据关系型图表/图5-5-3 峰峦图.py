# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:38:56 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import pandas as pd
import numpy as np
from plotnine import *
from scipy import interpolate
df=pd.read_csv('Facting_Data.csv')
df_melt=pd.melt(df,id_vars='X_Axis',var_name='var',value_name='value')
mydata=pd.DataFrame( columns=['x','y','var'])       
list_var=np.unique(df_melt['var'])
N=300
for i in list_var:
    x=df.loc[:,'X_Axis']
    y=df.loc[:,i]
    f = interpolate.interp1d(x,y)#, kind='slinear')#kind='linear', 
    x_new=np.linspace(np.min(x),np.max(x),N)
    y_new=f(x_new)
    mydata = mydata.append(pd.DataFrame({'x': x_new,'y':y_new,'var':np.repeat(i,N)}))

height=8
mydata['var']=mydata['var'].astype("category",categories= np.unique(df_melt['var']),ordered=True)
mydata['spacing']=mydata['var'].values.codes*height

labels=np.unique(df_melt['var'])
breaks=np.arange(0,len(labels)*height,height)

base_plot=(ggplot())
for i in np.unique(df_melt['var'])[::-1]:
    mydata_temp=mydata[mydata['var']==i]
    base_plot=(base_plot+
               geom_linerange(mydata_temp,aes(x='x',ymin='spacing',ymax='y+spacing',color='y'),size=1)+
               geom_line(mydata_temp,aes(x='x',y='y+spacing'),color="black",size=0.5))
base_plot=(base_plot+scale_color_cmap(name ='Spectral_r')+
           scale_y_continuous(breaks=breaks,labels=labels)+
           guides(color=guide_colorbar(title='value'))+
           theme(dpi=100,figure_size=(6,5))) 
print(base_plot)
