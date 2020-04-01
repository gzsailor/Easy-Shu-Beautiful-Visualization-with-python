# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:55:44 2019

@author: Jie Zhang，微信公众号【EasyShu】，本代码源自《Python数据可视化之美》
"""
from matplotlib import pyplot as plt

#----------------------------Method 1------------------------------------------------------------
# pyplot方式
plt.figure()
#X = np.arange(0.01, 10, 0.01)
# 分成2*2，占用第1个子图
plt.subplot(221,facecolor='#2B9ACE')
#plt.plot(X, np.sin(X), 'r-')

# 分成2*2，占用第2个子图
plt.subplot(222,facecolor='#89BD54')
#plt.plot(X, np.cos(X), 'g-')

# 分成2*1，占用第2个子图(即占用2*2第3、4子图)
plt.subplot(212,facecolor='#E6E243')
#plt.bar(np.arange(6), np.array([2, 4, 1, 6, 3, 8]))
#plt.savefig('add_subplot1.pdf',format='pdf')
#plt.suptitle('pyplot')
plt.show()


#-----------------------------Method 2-----------------------------------------------------------
# axes方式一：add_subplot
# 参数同plt.subplot一致
fig = plt.figure()
ax1 = fig.add_subplot(221,facecolor='#2B9ACE')
#ax1.plot(X, np.sin(X), 'r-')

ax2 = fig.add_subplot(222,facecolor='#89BD54')
#ax2.plot(X, np.cos(X), 'g-')

ax3 = fig.add_subplot(212,facecolor='#E6E243')
#ax3.bar(np.arange(6), np.array([2, 4, 1, 6, 3, 8]))

#fig.suptitle('add_subplot')
#plt.savefig('add_subplot2.pdf',format='pdf')
plt.show()

#-------------------------------Method 3---------------------------------------------------------
# axes方式二：subplots
# 相比add_subplot，函数调用比较简洁，但是不能自定义子图布局
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(8, 6))
#X = np.arange(0.01, 10, 0.01)
#ax[0, 0].plot(X, 2 * X - 1)
ax[0, 0].set_facecolor("#8F4B99")

#ax[0, 1].plot(X, np.log(X))
ax[0, 1].set_facecolor("#89BD54")

#ax[1, 0].plot(X, np.exp(X))
ax[1, 0].set_facecolor("#E6E243")

#ax[1, 1].plot(X, np.sin(X))
ax[1, 1].set_facecolor("#2B9ACE")
  
#plt.savefig('add_subplot3.pdf',format='pdf')
#fig.suptitle('subplots')
plt.show()

#----------------------------Method 4-----------------------------------------------------------------

plt.subplot2grid((2,3),(0,0),colspan=2,facecolor='#2B9ACE')
plt.subplot2grid((2,3),(0,2),facecolor='#E6E243')
plt.subplot2grid((2,3),(1,0),colspan=3,facecolor='#89BD54')
#plt.savefig('add_subplot4.pdf',format='pdf')
plt.show()

#---------------------------Method 5-------------------------------------------------

#from pylab import *
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(2, 3)

axes_1 = plt.subplot(G[0, 0:2],facecolor='#2B9ACE')
#xticks([]), yticks([])
#text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = plt.subplot(G[0,2],facecolor='#E6E243')
#xticks([]), yticks([])
#text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = plt.subplot(G[1, :],facecolor='#89BD54')
#xticks([]), yticks([])
#text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

#plt.savefig("add_subplot5.pdf")
#plt.savefig('../figures/gridspec.png', dpi=64)
plt.show()


#-----------------------------Method 6-------------------------------------------------
plt.axes([0.1,0.1,.8,.8],facecolor='#E6E243')
#plt.xticks([]), plt.yticks([])
#plt.text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

plt.axes([0.2,0.2,.3,.3],facecolor='#2B9ACE')
#plt.xticks([]), plt.yticks([])
#plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)
#plt.savefig("add_subplot6.pdf")
#plt.plt.savefig("../figures/axes.png",dpi=64)
plt.show()

#------------------------------Method 7-----------------------------------------
plt.axes([0.1,0.1,.5,.5],facecolor='#8F4B99')
#plt.xticks([]), plt.yticks([])
#plt.text(0.1,0.1, 'axes([0.1,0.1,.8,.8])',ha='left',va='center',size=16,alpha=.5)

plt.axes([0.2,0.2,.5,.5],facecolor='#89BD54')
#plt.xticks([]), plt.yticks([])
#plt.text(0.1,0.1, 'axes([0.2,0.2,.5,.5])',ha='left',va='center',size=16,alpha=.5)

plt.axes([0.3,0.3,.5,.5],facecolor='#E6E243')
#plt.xticks([]), plt.yticks([])
#plt.text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

plt.axes([0.4,0.4,.5,.5],facecolor='#2B9ACE')
#plt.xticks([]), plt.yticks([])
#plt.text(0.1,0.1, 'axes([0.4,0.4,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#plt.savefig("add_subplot7.pdf")
plt.show()
