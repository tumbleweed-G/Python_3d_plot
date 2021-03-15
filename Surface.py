import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Tamanho do chart na interface
fig = plt.figure(figsize = (10, 5))

#Plota para sair em 3d, quando configuramos projection para '3d' 
ax = fig.add_subplot(111, projection ='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

#definindo a superficie da esfera
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, rstride = 4, cstride = 4, color = 'b')

#mostra o grafico
plt.show()