import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Tamanho do chart na interface
fig = plt.figure(figsize = (10, 10))

#Define para sair em 3d, quando configuramos projection para '3d' 
ax = fig.add_subplot(111, projection ='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2), 
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
w = np.sqrt(2.0/3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)

#Plota o grafico
ax.quiver(x, y, z, u, v, w, length = 0.1)

#mostra o grafico
plt.show()