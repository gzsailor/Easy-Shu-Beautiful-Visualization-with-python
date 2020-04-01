# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:47:45 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""


from plotnine import *
from plotnine.data import mpg


t1=(t + facet_grid('.~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1.3,
        dpi=100,
       figure_size=(10,10)))
print(t1)
#t1.save('分面1.pdf')


t2=(t + facet_grid('year ~ .')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =0.5,
        dpi=100,
       figure_size=(4,4)))
print(t2)
#t2.save('分面2.pdf')

t3=(t + facet_grid('year ~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t3)
#t3.save('分面3.pdf')

t4=(t + facet_wrap('~ fl')
+theme_matplotlib()
+ theme(text=element_text(size=14,colour = "black"),
        strip_text=element_text(size=20,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t4)
#t4.save('分面4.pdf')


t5=(t + facet_grid('drv ~ fl', scales = "free")
+theme_matplotlib()
+ theme(text=element_text(size=12,colour = "black"),
        strip_text=element_text(size=15,colour = "black"),
        strip_background=element_rect(color='k'),
        aspect_ratio =1,
        dpi=100,
       figure_size=(9,9)))
print(t5)
#t5.save('分面5.pdf')