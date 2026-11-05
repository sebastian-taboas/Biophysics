# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:11:07 2024

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
D_u = 0.16       # Difusión para u
D_v = 0.08       # Difusión para v
dx = 1.0         # Tamaño de celda espacial
dt = 0.25        # Paso de tiempo aún más reducido para control preciso
n = 200          # Tamaño de la malla aumentado para patrones detallados


u = 1.0 - 0.2 * np.random.rand(n, n)
v = 0.2 * np.random.rand(n, n)


F = 0.035 + 0.003 * np.random.rand(n, n)  
k = 0.06 + 0.003 * np.random.rand(n, n)   


def laplacian(Z):
    return (np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4 * Z) / dx**2


num_steps = 3000  # Número de pasos de tiempo para observar patrones intermedios
for step in range(num_steps):
    
    Lu = laplacian(u)
    Lv = laplacian(v)
    

    du = D_u * Lu - u * v**2 + F * (1 - u)
    dv = D_v * Lv + u * v**2 - (F + k) * v
    
    u += dt * du
    v += dt * dv
    
 
    u = np.clip(u, 0, 1)
    v = np.clip(v, 0, 1)

   
    if step % 500 == 0:
        plt.imshow(u, cmap='copper', vmin=0, vmax=1)
        plt.title(f'Step {step}')
        plt.axis('off')
        plt.show()
