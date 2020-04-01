# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:51:28 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""

import numpy as np
import pandas as pd
from plotnine import *
df=pd.DataFrame(dict(x=np.random.normal(loc=10,scale=1,size=250)))
base_plot=(ggplot(df, aes(sample = 'x'))+
  geom_qq(shape='o',fill="none")+
  geom_qq_line()+
   theme(
       #text=element_text(size=15,face="plain",color="black"),
       axis_title=element_text(size=18,face="plain",color="black"),
       axis_text = element_text(size=16,face="plain",color="black"),
       aspect_ratio =1.05,
       figure_size = (5,5),
       dpi = 100
       )
  )
print(base_plot)

