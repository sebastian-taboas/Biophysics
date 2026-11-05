# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:47:08 2024

@author: Muá
"""
import numpy as np
# from scipy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def vdp(t, z):
    x, y = z
    return [y, mu*(1 - x**2)*y - x]

a, b = 0, 20

mus = [0, 1, 2]
styles = ["-", "--", ":"]
t = np.linspace(a, b, 500)

plt.figure(figsize=(14, 6))

for mu, style in zip(mus, styles):
    sol = solve_ivp(vdp, [a, b], [1, 0], method='LSODA', t_eval=t)
    plt.subplot(1, 2, 1)
    plt.plot(sol.t, sol.y[0], style, label=f"$\mu={mu}$")
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.xlim([-1, 21]) 
    plt.subplot(1, 2, 2)
    plt.plot(sol.y[0], sol.y[1], style, label=f"$\mu={mu}$")
    plt.xlabel('$y$')
    plt.ylabel('$x$')

plt.subplot(1, 2, 1)
plt.legend(loc="upper left", frameon=False)
plt.subplot(1, 2, 2)
plt.legend(loc="upper left", frameon=False)
plt.gca().set_aspect('equal')
plt.tight_layout()
# plt.savefig("C:\\Users\\Usuario\\Desktop\\VanderPol01.png", dpi=600)
plt.show()

