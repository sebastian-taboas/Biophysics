import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,100)
a = 0.5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softplus(x):
    return np.log(np.exp(x) + 1)

def celu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] > 0:
            y[i] = x[i]
        elif x[i] < 0:
            y[i] = a * (np.exp(x[i]/a) - 1)
        else:
            y[i] = 0
    return y

def elu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] == 0:
            y[i] = 0
        elif x[i] < 0:
            y[i] = a * np.exp(x[i]) - 1
        else:
            y[i] = x[i]
    return y

def exponential(x):
    return np.exp(x)

def gelu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i]= x[i] * (1 + math.erf(x[i] / np.sqrt(2)))/2
    return y

# glu(x) = x[n:]*sigmoid(x[:n])

# hard_shrink¿?¿?

def hard_sigmoid(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= -3:
            y[i] = 0
        elif x[i] >= 3:
            y[i] = 1
        else:
            y[i] = x[i]/6 + 0.5
    return y

def hard_silu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < -3:
            y[i] = 0
        elif x[i] > 3:
            y[i] = x[i]
        else:
            y[i] = x[i] * (x[i] + 3) / 6
    return y

def hard_tanh(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < -1:
            y[i] = -1
        elif x[i] > 1:
            y[i] = 1
        else:
            y[i] = x[i] 
    return y

def leaky_relu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < -0:
            y[i] = 0.1*x[i]
        else:
            y[i] = x[i]
    return y

def linear(x):
    return x

def log_sigmoid(x):
    return np.log(sigmoid(x))

# log_softmax ?¿?¿ np.log(softmax(x))

def mish(x):
    return x * np.tanh(softplus(x))

def relu(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if 0 < x[i]:
            y[i] = x[i]
        elif 0 >= x[i]:
            y[i] = 0
    return y

def relu6(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if 6 > relu(x)[i]:
            y[i] = relu(x)[i]
        elif 6 <= relu(x)[i]:
            y[i] = 6
    return y

def selu(x):
    alpha = 1.67326324 
    scale = 1.05070098

    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] > 0:
            y[i] = scale * x[i]
        else:
            y[i] = scale * alpha * (np.exp(x[i]) - 1)
    return y

def silu(x):
    return x * sigmoid(x)

# softmax ¿?¿? exp(x) / sum(exp(x))

def soft_shrink(x, lim):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] > lim:
            y[i] = x[i] - lim
        elif x[i] < -lim:
            y[i] = x[i] + lim
        else:
            y[i] = 0
    return y

def softsign(x):
    return x / (np.abs(x) + 1)

def sparse_plus(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= -1:
            y[i] = 0
        elif x[i]>= 1:
            y[i] = x[i]
        else:
            y[i] = (1/4) * (x[i] + 1)**2 
    return y

def sparse_sigmoid(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= -1:
            y[i] = 0
        if x[i] >= 1:
            y[i] = 1
        else:
            y[i] = 0.5 * (x[i] + 1)
    return y

# sparsemax ¿?¿? sparsemax(x)[i, j] = max(x[i, j] - τ(x[i, :]), 0).

def squareplus(x, b): # b = 4 default
    return (x + np.sqrt(x**2 + b)) / 2

def tanh(x):
    return np.tanh(x)

def tanh_shrink(x):
    return x - tanh(x)

def threshold(x, lim):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] > lim:
            y[i] = x[i]
        else:
            y[i] = lim
    return y

fig, axs = plt.subplots(5,5, figsize=(30, 14))

axs[0,0].plot(x,linear(x), label = 'linear')
axs[0,1].plot(x,exponential(x), label = 'exponential')

axs[0,2].plot(x,relu(x), label = 'relu')
axs[0,3].plot(x,relu6(x), label = 'relu6')
axs[0,4].plot(x,leaky_relu(x), label = 'leaky_relu')
axs[1,0].plot(x,elu(x), label = 'elu')
axs[1,1].plot(x,celu(x), label = 'celu')
axs[1,2].plot(x,selu(x), label = 'selu')

axs[1,3].plot(x,sigmoid(x), label = 'sigmoid')
axs[1,4].plot(x,hard_sigmoid(x), label = 'hard_sigmoid')
axs[2,0].plot(x,log_sigmoid(x), label = 'log_sigmoid')
axs[2,1].plot(x,tanh(x), label = 'tanh')
axs[2,2].plot(x,hard_tanh(x), label = 'hard_tanh')
axs[2,3].plot(x,tanh_shrink(x), label = 'tanh_shrink')

axs[2,4].plot(x,silu(x), label = 'silu')
axs[3,0].plot(x,hard_silu(x), label = 'hard_silu')

axs[3,1].plot(x,softsign(x), label = 'softsign')
axs[3,2].plot(x,sparse_plus(x), label = 'sparse_plus')
axs[3,3].plot(x,sparse_sigmoid(x), label = 'sparse_sigmoid')
axs[3,4].plot(x,squareplus(x,4), label = 'squareplus')
axs[4,0].plot(x,soft_shrink(x,a), label = 'soft_shrink')

axs[4,1].plot(x,gelu(x), label = 'gelu')

axs[4,2].plot(x,softplus(x), label = 'softplus')
axs[4,3].plot(x,mish(x), label = 'mish')

axs[4,4].plot(x,threshold(x,3), label = 'threshold')

for i in range(5):
    for j in range(5):
        axs[i,j].legend(loc='upper left')

plt.tight_layout()
fig.show()
plt.savefig("C:/Users/sebas/Desktop/Uni/Grao Física/4º fisica/biofisica/traballo1_redes_neuronais/layers.pdf", dpi = 600)


# mish x * sigmoid(x)
# silu x * np.tanh(softplus(x))
# gelu y[i]= x[i] * (1 + math.erf(x[i] / np.sqrt(2)))/2