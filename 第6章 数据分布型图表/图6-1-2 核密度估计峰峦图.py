# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:29:39 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
import pandas as pd
import numpy as np
import joypy
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
plt.rc('font',family='Times New Roman')

#----------------------------------(a) ------------------------------------------
sns.set_context("notebook", font_scale=1.5,
                rc={'font.size': 12, 
                    'axes.labelsize': 20, 'legend.fontsize':15, 
                    'xtick.labelsize': 15,'ytick.labelsize': 15})

df = pd.read_csv("lincoln_weather.csv")
Categories=['January', 'February', 'March', 'April', 'May', 'June','July',
            'August','September', 'October', 'November','December']
df['Month']=df['Month'].astype("category",categories=Categories,ordered=True)

fig, axes = joypy.joyplot(df, column=["Mean.Temperature..F."], 
                          by="Month", ylim='own',colormap=cm.Spectral_r,#color='#FF8B19',
                          #hist=True,bins=30,
                          alpha= 0.9,figsize=(6,5))
plt.xlabel("Mean Temperature",{'size': 15 })
plt.ylabel("Month",{'size': 15 })
#axes.set_axis_labels("Mean Temperature", "Month")   
#plt.show()
#fig.savefig('joyplot.pdf')

#----------------------------------(b) ------------------------------------------
#import numpy as np
#从scipy库中导入插值需要的方法 interpolate
from scipy import interpolate
from sklearn.neighbors import KernelDensity
from plotnine import *


def df_split(df,f):
   list_f=np.unique(df[f])
   splitdata=[]
   for i in list_f:
       splitdata.append(df[df[f]==i])
   return splitdata

df = pd.read_csv("lincoln_weather.csv")
Categories=['January', 'February', 'March', 'April', 'May', 'June','July',
            'August','September', 'October', 'November','December']
df['Month']=df['Month'].astype("category",categories=Categories,ordered=True)

#定义函数 x:横坐标列表 y:纵坐标列表 kind:插值方式
dt=df[["Month","Mean.Temperature..F."]]
#dt=dt.set_index(["Month"])
splitdata=df_split(dt,f='Month')


xmax=max(dt["Mean.Temperature..F."])*1.1
xmin=min(dt["Mean.Temperature..F."])*0.9


N=len(splitdata)
labels_y=np.unique(df['Month'])

mydata=pd.DataFrame(columns = ["variable", "x", "y"]) #创建空的Data.Frame

X_plot = np.linspace(xmin, xmax, 200)[:, np.newaxis]

for i in range(0,N):
    X=np.array(splitdata[i]["Mean.Temperature..F."])[:, np.newaxis]
    kde = KernelDensity(kernel='gaussian', bandwidth=3.37).fit(X)
    Y_dens =np.exp( kde.score_samples(X_plot))
    mydata_temp=pd.DataFrame({"variable":np.repeat(splitdata[i]['Month'][0],len(X_plot)),
                          "x":X_plot.flatten(), "y":Y_dens})
    mydata=mydata.append(mydata_temp)    

Categories=['January', 'February', 'March', 'April', 'May', 'June','July',
            'August','September', 'October', 'November','December']
mydata['variable']=mydata['variable'].astype("category",categories=Categories,ordered=True)
mydata['num_variable']=pd.factorize(mydata['variable'], sort=True)[0]

Step=max(mydata['y'])*0.3
mydata['offest']=-mydata['num_variable']*Step
mydata['density_offest']=mydata['offest']+mydata['y']

p=(ggplot())
for i in range(0,N):
    p=(p+ geom_linerange(mydata[mydata['num_variable']==i],
                         aes(x='x',ymin='offest',ymax='density_offest',
                             group='variable',color='y'),
                             size =1, alpha =1)+
       geom_line(mydata[mydata['num_variable']==i],
                 aes(x='x', y='density_offest'),color="black",size=0.5))
                         
p=(p+scale_color_cmap(name ='Spectral_r')+
  scale_y_continuous(breaks=np.arange(0,-Step*N,-Step),
                     #limits=(max(mydata['density_offest']),-Step*(N-1)),
                     labels=Categories)+
  xlab("Mean Temperature")+
  ylab("Month")+
  guides(color = guide_colorbar(title="Density",
                                barwidth  = 15, 
                                barheight = 70))+
  theme_classic()+
  theme(
    panel_background=element_rect(fill="white"),
    panel_grid_major_x = element_line(colour = "#E5E5E5",size=.75),
    panel_grid_major_y = element_line(colour = "grey",size=.25),
    axis_line = element_blank(),
    text=element_text(size=12,colour = "black"),
    plot_title=element_text(size=15,hjust=.5),
    legend_position="right",
    
    aspect_ratio =1.05,
    dpi=100,
    figure_size=(5,5)
  ))
print(p)
#p.save("joyplot2.pdf")    
