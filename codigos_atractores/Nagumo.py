# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:34:10 2023

@author: Muá
"""

import numpy as np
import matplotlib.pyplot as plt




I1_1=0.1
a1_1=0.15
b1_1=0.14
g1_1=2.5

I1_3=0.01
a1_3=0.15
b1_3=0.14
g1_3=2.5

I1_2=0.1
a1_2=0.2
b1_2=0.001
g1_2=2.5

I1_4=0.1
a1_4=0.2
b1_4=0.08
g1_4=2.5

I2=0.
a2=0.15
b2=0.001
g2=5.75

I3=0.
a3=0.15
b3=0.01
g3=7.


x01_1=0.5
y01_1=-0.0905
x01_2=0.5
y01_2=-0.0905
x01_3=1.
y01_3=-1.
x01_4=0.5
y01_4=--0.0905

x02=0.5
y02=-0.0905

x03=1.
y03=1.

t01_1=0.
t01_2=0.
t01_3=0
t01_4=0
t02=0.
t03=0.
deltat=0.001


def f(x,y,a,I):
    m=I - x*(x-a)*(x-1.) - y
    return m

def h(x,y,b,g):
    m= b*(x-g*y)
    return m

def ceroclina1(s,a,I):
    w=I - s*(s-a)*(s-1.)
    return w
def ceroclina2(s,g):
    w=s/g
    return w

n=1000000
n3=100000

x1_1=np.zeros(n3)
y1_1=np.zeros(n3)
t1_1=np.zeros(n3)

x1_3=np.zeros(n)
y1_3=np.zeros(n)
t1_3=np.zeros(n)

x1_2=np.zeros(n)
y1_2=np.zeros(n)
t1_2=np.zeros(n)

x1_4=np.zeros(n)
y1_4=np.zeros(n)
t1_4=np.zeros(n)

x2=np.zeros(n)
y2=np.zeros(n)
t2=np.zeros(n)

x3=np.zeros(n3)
y3=np.zeros(n3)
t3=np.zeros(n3)

xcero=np.linspace(-0.5,1.5,10000)

for i in range(n3):

    k1x=deltat*f(x01_1,y01_1,a1_1,I1_1)
    k1y=deltat*h(x01_1,y01_1,b1_1,g1_1)
    
    k2x=deltat*f(x01_1 +(1./2)*k1x,y01_1 + (1./2)*k1y,a1_1,I1_1)
    k2y=deltat*h(x01_1 +(1./2)*k1x,y01_1 + (1./2)*k1y,b1_1,g1_1)
    
    k3x=deltat*f(x01_1 +(1./2)*k2x,y01_1 + (1./2)*k2y,a1_1,I1_1)
    k3y=deltat*h(x01_1 +(1./2)*k2x,y01_1 + (1./2)*k2y,b1_1,g1_1)
    
    k4x=deltat*f(x01_1 +k3x,y01_1 + k3y,a1_1,I1_1)
    k4y=deltat*h(x01_1 +k3x,y01_1 + k3y,b1_1,g1_1)

    x1_1[i]= x01_1 + k1x/6. + k2x/3. + k3x/3 + k4x/6.
    y1_1[i]= y01_1 + k1y/6. + k2y/3. + k3y/3. + k4y/6.
    t1_1[i]= t01_1 + deltat
    

    x01_1=x1_1[i]
    y01_1=y1_1[i]
    t01_1=t1_1[i]
    
for i in range(n):

    k1x=deltat*f(x01_4,y01_4,a1_4,I1_4)
    k1y=deltat*h(x01_4,y01_4,b1_4,g1_4)
    
    k2x=deltat*f(x01_4 +(1./2)*k1x,y01_4 + (1./2)*k1y,a1_4,I1_4)
    k2y=deltat*h(x01_4 +(1./2)*k1x,y01_4 + (1./2)*k1y,b1_4,g1_4)
    
    k3x=deltat*f(x01_4 +(1./2)*k2x,y01_4 + (1./2)*k2y,a1_4,I1_4)
    k3y=deltat*h(x01_4 +(1./2)*k2x,y01_4 + (1./2)*k2y,b1_4,g1_4)
    
    k4x=deltat*f(x01_4 +k3x,y01_4 + k3y,a1_4,I1_4)
    k4y=deltat*h(x01_4 +k3x,y01_4 + k3y,b1_4,g1_4)

    x1_4[i]= x01_4 + k1x/6. + k2x/3. + k3x/3 + k4x/6.
    y1_4[i]= y01_4 + k1y/6. + k2y/3. + k3y/3. + k4y/6.
    t1_4[i]= t01_4 + deltat
 
    x01_4=x1_4[i]
    y01_4=y1_4[i]
    t01_4=t1_4[i]

for i in range(n):
    k1x=deltat*f(x01_2,y01_2,a1_2,I1_2)
    k1y=deltat*h(x01_2,y01_2,b1_2,g1_2)
    
    k2x=deltat*f(x01_2 +(1./2)*k1x,y01_2 + (1./2)*k1y,a1_2,I1_2)
    k2y=deltat*h(x01_2 +(1./2)*k1x,y01_2 + (1./2)*k1y,b1_2,g1_2)
    
    k3x=deltat*f(x01_2 +(1./2)*k2x,y01_2 + (1./2)*k2y,a1_2,I1_2)
    k3y=deltat*h(x01_2 +(1./2)*k2x,y01_2 + (1./2)*k2y,b1_2,g1_2)
    
    k4x=deltat*f(x01_2 +k3x,y01_2 + k3y,a1_2,I1_2)
    k4y=deltat*h(x01_2 +k3x,y01_2 + k3y,b1_2,g1_2)
    
    x1_2[i]= x01_2 + k1x/6. + k2x/3. + k3x/3 + k4x/6.
    y1_2[i]= y01_2 + k1y/6. + k2y/3. + k3y/3. + k4y/6.
    t1_2[i]= t01_2 + deltat

    x01_2=x1_2[i]
    y01_2=y1_2[i]
    t01_2=t1_2[i]    
    
 
for i in range(n):

    k1x=deltat*f(x01_3,y01_3,a1_3,I1_3)
    k1y=deltat*h(x01_3,y01_3,b1_3,g1_3)
    
    k2x=deltat*f(x01_3 +(1./2)*k1x,y01_3 + (1./2)*k1y,a1_3,I1_3)
    k2y=deltat*h(x01_3 +(1./2)*k1x,y01_3 + (1./2)*k1y,b1_3,g1_3)
    
    k3x=deltat*f(x01_3 +(1./2)*k2x,y01_3 + (1./2)*k2y,a1_3,I1_3)
    k3y=deltat*h(x01_3 +(1./2)*k2x,y01_3 + (1./2)*k2y,b1_3,g1_3)
    
    k4x=deltat*f(x01_3 +k3x,y01_3 + k3y,a1_1,I1_3)
    k4y=deltat*h(x01_3 +k3x,y01_3 + k3y,b1_1,g1_3)
    
    x1_3[i]= x01_3 + k1x/6. + k2x/3. + k3x/3 + k4x/6.
    y1_3[i]= y01_3 + k1y/6. + k2y/3. + k3y/3. + k4y/6.
    t1_3[i]= t01_3 + deltat
    
    x01_3=x1_3[i]
    y01_3=y1_3[i]
    t01_3=t1_3[i]
    

fig = plt.figure(figsize=(9, 7))

fig = plt.figure(figsize=(9, 7)) 

ax1 = fig.add_subplot(3, 2, 1)
ax1.plot(x1_3,y1_3,'b')
ax1.plot(xcero,ceroclina1(xcero,a1_3,I1_3),'g-',label='ceroclina: dv=0')
ax1.plot(xcero,ceroclina2(xcero,g1_3),color='orange',label='ceroclina: dw=0')
ax1.set_xlabel('v', fontsize='13')
ax1.set_ylabel('w', fontsize='13')
#ax1.text(0.45,0.95,'A')
ax1.grid()
ax1.legend(loc='best')
ax1.set_ylim((-0.6,0.8))
ax1.set_xlim((-0.6,1.5))  

ax2 = fig.add_subplot(3,2,2)
ax2.plot(t1_3,x1_3,'g',label='v')
ax2.plot(t1_3,y1_3,color='orange',label='w')
ax2.legend(loc='best')
ax2.set_xlabel('Tiempo', fontsize='13')
ax2.set_ylabel('v y w', fontsize='13')
#ax2.text(0.45, 0.95,'B')
ax2.set_ylim((-1.5,1.5))
ax2.set_xlim((-3,40))
ax2.grid()

ax3 = fig.add_subplot(3,2,3)
ax3.plot(x1_4,y1_4,'b')
ax3.plot(xcero,ceroclina1(xcero,a1_4,I1_4),'g-',label='ceroclina:dv=0')
ax3.plot(xcero,ceroclina2(xcero,g1_4),color='orange',label='ceroclina:dw=0')
ax3.legend(loc='best')
ax3.set_xlabel('v', fontsize='13')
ax3.set_ylabel('w', fontsize='13')
#ax3.text(0.45, 0.95,'C')
ax3.set_ylim((-0.3,0.8))
ax3.set_xlim((-0.6,1.5))
ax3.grid()

ax4 = fig.add_subplot(3,2,4)
ax4.plot(t1_4,x1_4,'g',label='v')
ax4.plot(t1_4,y1_4,color='orange',label='w')
ax4.legend(loc='best')
ax4.set_xlabel('Tiempo', fontsize='13')
ax4.set_ylabel('v y w', fontsize='13')
#ax4.text(0.45, 0.95,'D')
ax4.grid()
ax4.set_ylim((-0.3,0.8))
ax4.set_xlim((-0.6,200))

ax5 = fig.add_subplot(3,2,5)
ax5.plot(x1_2,y1_2,'b')
ax5.plot(xcero,ceroclina1(xcero,a1_2,I1_2),'g-',label='ceroclina: dv=0')
ax5.plot(xcero,ceroclina2(xcero,g1_2),color='orange',label='ceroclina: dw=0')
ax5.set_xlabel('v', fontsize='13')
ax5.set_ylabel('w', fontsize='13')
#ax5.text(0.45, 0.95,'E')
ax5.legend(loc='best')
ax5.grid()
ax5.set_ylim((-0.3,0.8))
ax5.set_xlim((-0.6,1.5))

ax6 = fig.add_subplot(3,2,6)
ax6.plot(t1_2,x1_2,'g',label='v')
ax6.plot(t1_2,y1_2,color='orange',label='w')
#ax6.text(0.45, 0.95,'F')
ax6.legend(loc='best')
ax6.set_xlabel('Tiempo', fontsize='13')
ax6.set_ylabel('v y w', fontsize='13')
ax6.grid()


fig.tight_layout()
# fig.savefig(".codigos_atractores/multiplePlots1window.svg", dpi=600)
fig.show()