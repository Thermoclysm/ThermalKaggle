# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:46:01 2018

@author: TB18
"""

import pandas as pd
import matplotlib.pyplot as plt



#%%

df0 = pd.read_csv("datasets/train_V2.csv")

#%%

df0.head()

#slice for quick testing
df1 = df0[:150]

#plt.figure(1)
#plt.plot(df1['damageDealt'], df1['kills'], 'bx')
#
#plt.figure(2)
#plt.hist(df1['kills'])
#plt.show()

#%%
plt.figure(1)
plt.scatter(df1['damageDealt'], df1['kills'], s=df1['winPlacePerc']*20)
plt.figure(2)
plt.scatter(df1['walkDistance'], df1['winPlacePerc'])

#%%
plt.figure(3)
plt.scatter(df0['walkDistance'], df0['winPlacePerc'])
