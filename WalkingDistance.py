# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:55:17 2018

@author: SFbwt

Looking at win percentage as a function of walking distance
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#%%

df0 = pd.read_csv("datasets/train_V2.csv")

#%%
#slice for quick testing
df1 = df0[:150]
plt.figure(1)
plt.scatter(df1['walkDistance'], df1['winPlacePerc'])

#%%
"""bin data by distance walked then compute the mean win percentage per bin"""
mu1=[]
sig1 =[]
sige1 = []
bin_width= 100
max_dist = 10000
no_bins = int(max_dist/bin_width)
bin_edges= [i*bin_width for i in range(0,no_bins)]
def bin_walks(data0, mean_win, stdev_win, stderr_win):



    for j in range(len(bin_edges)-2):
        data2 = data0[(data0['walkDistance']>=bin_edges[j]) & \
        (data0['walkDistance']<bin_edges[j+1])]
        mean_win.append(data2['winPlacePerc'].mean())
        #fucked if I know what is appropriate just want measure of variance
        stdev_win.append(data2['winPlacePerc'].std())
        stderr_win.append(data2['winPlacePerc'].sem())

bin_walks(df0, mu1, sig1, sige1)
#%%
#scale this shit up
sige1 = [i*10 for i in sige1]
#%%
plt.figure(2)
plt.title("Average win percentage for binned walking distances")
plt.scatter(bin_edges[:-2],mu1)
plt.ylim(ymin=0,ymax=1.25)
plt.errorbar(bin_edges[:-2], mu1, yerr=sige1)

#%%
"""restrict to solo fpp games only"""

dfsf = df0[df0['matchType']=='solo-fpp']
mu2=[]
sig2 =[]
sige2 = []
bin_walks(dfsf, mu2, sig2, sige2)

plt.figure(3)
plt.title("Average win percentage for binned walking distances")
plt.scatter(bin_edges[:-2],mu1, label='all matches')
plt.ylim(ymin=0,ymax=1.25)
plt.errorbar(bin_edges[:-2], mu1, yerr=sige1, marker='x')
plt.scatter(bin_edges[:-2],mu2, label='solo only', marker='+')
plt.ylim(ymin=0,ymax=1.25)
plt.errorbar(bin_edges[:-2], mu2, yerr=sige2)
plt.legend(loc='best')


#%%
"""initial fit test using logistic function"""

def log4p(x, x0, L, k):
    return L/(1+np.exp(-k*(x-x0)))
    
xtest = np.linspace(0, 10000, 1000)
ytest = log4p(xtest, 2200, 1, 0.5)
    
popt, pcov = curve_fit(log4p, bin_edges[:-2], mu1, bounds=((1000,0.8,0),(2500,0.9,0.05)))
popt

plt.plot(bin_edges[:-2], log4p(bin_edges[:-2], *popt), 'r--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

    