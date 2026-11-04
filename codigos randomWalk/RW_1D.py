import numpy as np
import matplotlib.pyplot as plt
def Randomwalk1D(n): 
   x = 0
   y = 0
   xposition = [0] 
   yposition = [0] 

   for i in range (1,n+1):
       step = np.random.uniform(0,1)

       if step < 0.5: 
           x += 1
           y += 1 

       if step > 0.5: 
           x += 1
           y += -1 
 
       xposition.append(x)
       yposition.append(y)

   return [xposition,yposition]


number_of_RW = 10

for i in range(number_of_RW):
    Randwalk = Randomwalk1D(1000) 
    plt.plot(Randwalk[0],Randwalk[1],'r-', label = "Randwalk1D") 
plt.show()