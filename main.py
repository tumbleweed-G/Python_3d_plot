import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Esta relacionado com o tamanho da legenda
mpl.rcParams['legend.fontsize'] = 10

#Tamanho do chart na interface
fig = plt.figure(figsize = (10, 5))
#plota para sair em 3d, quando configuramos projection para '3d' 
ax = fig.gca(projection = '3d')
#intervalos de theta que serão gerados, pela função linspace
#Essa funcao cria uma sequencia dentro de um intervalo, o ultimo argumento do metodo
#gera a quantidade de pontos dentro do intervalo, em analise
theta = np.linspace(-4*np.pi, 4*np.pi, 100)

#intervalos de theta que serão gerados, pela função linspace
z = np.linspace(-2, 2, 100)

#Relaciona os pontos com as funcões que serão colocadas no gráfico
r = z **2 
x = r * np.sin(theta)
y = r * np.cos(theta)

#Entra com os valores em ordem alfabetica x, y, z no grafico
ax.plot(x, y, z, label = 'parametric curve')
ax.legend()

#mostra o grafico
plt.show()