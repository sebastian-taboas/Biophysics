# El caminar del borracho  
# Un paseo aleatorio en dos dimensiones  
# Se parte del punto (0,0) del plano cartesiano  
# Cada paso que se da es de longitud r  
# El ángulo con el que se da cada paso es aleatorio  
import random  
import math  
import matplotlib.pyplot as plt  
random.seed()  
n=100000 # número de pasos  
r=1 # longitud del paso  
x=y=0 # punto de partida (x,y)=(0,0)  
listax=[x]  
listay=[y]  
for i in range(n):  
  angulo=random.random()*math.pi*2 # en radianes  
  x+=r*math.cos(angulo)  
  y+=r*math.sin(angulo)  
  listax.append(x)  
  listay.append(y)  
plt.plot(listax,listay)  
plt.show()