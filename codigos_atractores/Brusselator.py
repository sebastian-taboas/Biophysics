#LOTKA-VOLTERRA SIMPLE

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
def df_dt(x, t, a, b):
    dx = 1-(b+1)*x[0]+a*x[0]*x[0]*x[1]
    dy = b* x[0] -a*x[0]*x[0]*x[1]
    return np.array([dx, dy])
"""
puntos interesantes a=1 y b = 2, es un atractor
si b > a+1 es inestable
si b < a+1 es estable

"""

a = 1
b = 2
c=b/a

x0 = 0
y0 = 0
condiciones_iniciales = np.array([x0, y0])

tf = 100
N = 1000
t = np.linspace(0, tf, N)

sol = integrate.odeint(df_dt, condiciones_iniciales, t, args=(a, b))

n_max = np.max(sol) * 1.10
x_max = np.max(sol[:,0]) * 1.05
y_max = np.max(sol[:,1]) * 1.05
x = np.linspace(0, x_max, 25)
y = np.linspace(0, y_max, 25)

xx, yy = np.meshgrid(x, y)
uu, vv = df_dt((xx, yy), 0, a, b)
norm = np.sqrt(uu**2 + vv**2)
uu = uu / norm
vv = vv / norm

fig, ax = plt.subplots(1,2)
fig.set_size_inches(14,5)

ax[1].quiver(xx, yy, uu, vv, norm, cmap=plt.cm.gray)
ax[1].plot(sol[:, 0], sol[:, 1], "r", lw=2, alpha=0.8)
ax[1].scatter(1, c, c="red", marker="+")
#ax[1].set_xlim(-0.1, x_max)
#ax[1].set_ylim(-0.1, y_max)
ax[1].set_xlabel('$X$', fontsize=14)
ax[1].set_ylabel('$Y$', fontsize=14)
#ax[1].markers_on = [1, c]
ax[0].plot(t, sol[:, 0], "b" ,label='$X$')
ax[0].plot(t, sol[:, 1], "r" ,label='$Y$')
ax[0].legend(loc='best', fontsize=14, frameon= False)
limit= tf+2
ax[0].set_xlim(-5, limit)
#ax[0].set_ylim(0, 75)
ax[0].set_xlabel('$t$', fontsize=14)
ax[0].set_ylabel('$X$, $Y$', fontsize=14)
fig.tight_layout()
# plt.savefig('C:\\Users\\pc\\Desktop\\brusselator.png', dpi=300)
plt.show()