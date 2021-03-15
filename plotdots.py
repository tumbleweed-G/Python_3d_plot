import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):

    return (vmax-vmin)*np.random.rand(n) + vmin

#Esta relacionado com o tamanho da legenda
mpl.rcParams['legend.fontsize'] = 10

#Tamanho do chart na interface
fig = plt.figure(figsize = (10, 5))

#Plota para sair em 3d, quando configuramos projection para '3d' 
ax = fig.add_subplot(111, projection ='3d')
n = 100

# Looping definindo pontos discretos aleatorios
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zl, zh)
    #Plota no grafico:
    ax.scatter(xs, ys, zs, c=c, marker=m)

#Legenda do Chart
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#mostra o grafico
plt.show()