# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:55:17 2018

@author: SFbwt

Looking at win percentage as a function of walking distance
"""

import pandas as pd
import matplotlib.pyplot as plt

#%%

df0 = pd.read_csv("datasets/train_V2.csv")

#%%
#slice for quick testing
df1 = df0[:150]
plt.figure(1)
plt.scatter(df1['walkDistance'], df1['winPlacePerc'])

#%%
"""bin data by distance walked then compute the mean win percentage per bin"""
bin_width= 100
max_dist = 10000
no_bins = int(max_dist/bin_width)
bin_edges= [i*bin_width for i in range(0,no_bins)]

#df2 = df1[(df1['walkDistance']>=0) & (df1['walkDistance']<500)]
#df2['walkDistance'].mean(), df2['winPlacePerc'].mean()
mean_win = []
#fucked if I know what is appropriate just want measure of variance
stdev_win = []
stderr_win = []
for j in range(len(bin_edges)-2):
    df2 = df0[(df0['walkDistance']>=bin_edges[j]) & \
    (df0['walkDistance']<bin_edges[j+1])]
    mean_win.append(df2['winPlacePerc'].mean())
    stdev_win.append(df2['winPlacePerc'].std())
    stderr_win.append(df2['winPlacePerc'].sem())
#%%
#scale this shit up
stderr_win = [i*10 for i in stderr_win]
plt.figure(2)
plt.scatter(bin_edges[:-2],mean_win)
plt.errorbar(bin_edges[:-2], mean_win, yerr=stderr_win)
    