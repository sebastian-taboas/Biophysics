import numpy as np
import matplotlib.pyplot as plt

def crea_ramdom_walk():
    x = np.random.choice([-1,1], size = 100, replace= True)
    return np.cumsum(x)

walks = int(input('Numero de paseos:'))

for i in range(walks):
    X = crea_ramdom_walk()
    plt.plot(X)
plt.show()
    