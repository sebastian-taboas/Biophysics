import numpy as np 
import matplotlib.pyplot as plt
import random 
n = 1000 
x = np.zeros(n) 
y = np.zeros(n) 
direction=["N","S","E","O"] 
for i in range(1, n): 
    step = random.choice(direction) 
    if step == "E": 
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif step == "O": 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif step == "N": 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
        
plt.plot(x,y)
plt.show()        