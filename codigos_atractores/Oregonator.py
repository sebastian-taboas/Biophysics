

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate


def df_dt(x, t, A, B, k1, k2, k3, k4, k5, k6, k7, k8, k9, f):
    dx = k1*A*x[1]-k2*x[0]*x[1]+k3*B*x[0]-2*k4*x[0]**2
    dy = -k5*A*x[1]-k6*x[0]*x[1]+f*k7*x[2]
    dz = k8*B*x[0]-k9*x[2]
    return np.array([dx, dy, dz])



A = 0.1  
B = 50
k1 = 1
k2 = 2
k3 = 6
k4 = 3
k5 = 1
k6 = 1
k7 = 0.8
k8 = 1
k9 = 1
f = 1


x0 = 10
y0 = 100
z0 = 100

condiciones_iniciales = np.array([x0, y0, z0])

tf = 100
N = 1000000
t = np.linspace(0, tf, N)

sol = integrate.odeint(df_dt, condiciones_iniciales, t, args=(A, B, k1, k2, k3, k4, k5, k6, k7, k8, k9, f))

fig=plt.figure(figsize=(12,5))

ax = fig.add_subplot(1,2,1)
ax.plot(t, sol[:, 0], "b" ,label='$X$')
ax.plot(t, sol[:, 1], "r" ,label='$Y$')
ax.plot(t, sol[:, 2], "g" ,label='$Z$')
ax.legend(loc='best', fontsize=14, frameon= False)

#ax[0].set_ylim(0, 75)
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$X$, $Y$', fontsize=14)

ax = fig.add_subplot(1,2,2, projection = '3d')
ax.plot(sol[:, 0],sol[:, 1],sol[:, 2])
ax.set_xlabel('$X$')
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')
ax.view_init(40, 35)
fig.tight_layout()
# plt.savefig('C:\\Users\\Usuario\\Desktop\\oregonator.png', dpi=300)
plt.show()