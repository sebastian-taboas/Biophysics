import random  
import math  
import matplotlib.pyplot as plt  
random.seed()  
n=[50, 500, 5000, 50000] # número de pasos  
r=0.5 # longitud del paso  
x1=y1=x2=y2=x3=y3=x4=y4=0 # punto de partida (x,y)=(0,0)  
lista1x=[x1]  
lista1y=[y1]
lista2x=[x2]  
lista2y=[y2] 
lista3x=[x3]  
lista3y=[y3] 
lista4x=[x4]  
lista4y=[y4]   
 
for i in range(n[0]):  
  angulo1=random.random()*math.pi*2  # en radianes  
  x1+=r*math.cos(angulo1)  
  y1+=r*math.sin(angulo1)    
  lista1x.append(x1)  
  lista1y.append(y1)
  
  
for i in range(n[1]):  
  angulo2=random.random()*math.pi*2
  x2+=r*math.cos(angulo2)  
  y2+=r*math.sin(angulo2)
  lista2x.append(x2)  
  lista2y.append(y2)

    
for i in range(n[2]):
  angulo3=random.random()*math.pi*2
  x3+=r*math.cos(angulo3)  
  y3+=r*math.sin(angulo3)
  lista3x.append(x3)  
  lista3y.append(y3)


for i in range(n[3]):
  angulo4=random.random()*math.pi*2  
  x4+=r*math.cos(angulo4)  
  y4+=r*math.sin(angulo4)     
  lista4x.append(x4)  
  lista4y.append(y4)
  
  
  
fig, axs = plt.subplots(2,2)
axs[0, 0].plot(lista1x,lista1y, 'k')
axs[0, 1].plot(lista2x,lista2y, 'k')
axs[1, 0].plot(lista3x,lista3y, 'k')
axs[1, 1].plot(lista4x,lista4y, 'k')

axs[0,0].axes.get_xaxis().set_visible(False)
axs[0,0].axes.get_yaxis().set_visible(False)
axs[0,0].legend(title='n=50', loc='best', frameon=False)
axs[0,1].axes.get_xaxis().set_visible(False)
axs[0,1].axes.get_yaxis().set_visible(False)
axs[0,1].legend(title='n=500', loc='best',frameon=False)
axs[1,0].axes.get_xaxis().set_visible(False)
axs[1,0].axes.get_yaxis().set_visible(False)
axs[1,0].legend(title='n=5000', loc='best', frameon=False)
axs[1,1].axes.get_xaxis().set_visible(False)
axs[1,1].axes.get_yaxis().set_visible(False)
axs[1,1].legend(title='n=50000', loc='best', frameon=False)
plt.tight_layout()
plt.savefig('codigos randomWalk/RandomWalk_Grafica=2.png', dpi=300)
fig.show()