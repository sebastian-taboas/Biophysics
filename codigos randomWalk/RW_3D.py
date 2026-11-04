# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:04:02 2022

@author: pc
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
N =1500
R = (np.random.rand(N)*6).astype("int") 
x = np.zeros(N) 
y = np.zeros(N)
z = np.zeros(N)
x[ R==0 ] = -1; x[ R==1 ] = 1 
y[ R==2 ] = -1; y[ R==3 ] = 1
z[ R==4 ] = -1; z[ R==5 ] = 1
x = np.cumsum(x) 
y = np.cumsum(y)
z = np.cumsum(z)
plt.figure()
ax = plt.subplot(1,1,1, projection='3d')
ax.plot(x, y, z) 
plt.show()