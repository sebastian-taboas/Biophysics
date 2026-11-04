
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Número de enlaces
N = 100
# Iteraciones para intentar encontrar una posición no superpuesta
MAX_ITER = 1000

# Longitud enlace
l = 1

# Ángulo enlace (grados)
theta = 120

plt.close("all")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(1):  # Puedes aumentar el rango para generar más cadenas
    resultados = np.zeros((N+1, 3))  # Inicializar las posiciones de los segmentos

    for j in range(3, N+1):  # Comenzar desde el tercer segmento
        success = False  # Variable para verificar si se ha añadido un segmento exitosamente
        for iteration in range(MAX_ITER):  
            # Generar un nuevo segmento
            angle = np.random.uniform(0, 2*np.pi)
            z_angle = np.arccos(2*np.random.uniform(0,1)-1)
            dx = l * np.sin(z_angle) * np.cos(angle)
            dy = l * np.sin(z_angle) * np.sin(angle)
            dz = l * np.cos(z_angle)
            
            new_position = resultados[j-1] + np.array([dx, dy, dz])

            # Verificar autoevitabilidad
            overlap = False
            for k in range(j-1):  
                distance = np.linalg.norm(new_position - resultados[k])
                if distance < l * 0.5:  
                    overlap = True
                    break

            if not overlap:  
                resultados[j] = new_position
                success = True
                break

        if not success:
            print(f"No se pudo evitar la superposición después de {MAX_ITER} intentos en el segmento {j}.")
            break  # Salir del bucle si no se pudo añadir un segmento exitosamente

    ax.plot(resultados[:, 0], resultados[:, 1], resultados[:, 2])
    ax.scatter(resultados[:, 0], resultados[:, 1], resultados[:, 2])

plt.show()



