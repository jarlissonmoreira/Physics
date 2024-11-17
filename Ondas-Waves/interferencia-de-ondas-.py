# Nesse script, vamos simular a interferência de duas ondas circulares.
# Por exemplo, duas pedras caindo em um lago, onde iremos calcular e plotar
# a superposição das duas ondas senoidais

import matplotlib.pyplot as plt
import numpy as np
import math

wavelength = 5.0          # comprimento de onda, em cm
k = 2*math.pi/wavelength  # constante do número de onda
xi0 = 1.0                 # amplitude da altura das ondas
separation = 20.0         # Separação dos centros, em cm
side = 100.0              # Lado do quadrado analisado, onde ocorrerão as interferências, em cm
points = 500              # Número de pontos da grid, em cada lado
spacing = side/points     # Espaçamento dos pontos


# Calculo das posições dos centros dos círculos
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Array para armazenar as alturas
xi = np.empty([points,points] ,float)

# Calculando os valores no array xi
# as variáveis i e j são os nossos pontos de coordenadas, da
# região (quadrada) analisada. Em cada posição, calculamos a superposição
for i in range(points):
  y = spacing*i
  for j in range(points):
    x = spacing*j
    r1 = math.sqrt((x-x1)**2+(y-y1)**2)
    r2 = math.sqrt((x-x2)**2+(y-y2)**2)
    xi[i,j] = xi0*math.sin(k*r1) + xi0*math.sin(k*r2) # superposição das ondas

# plot
plt.imshow(xi,origin="lower",extent=[0,side,0,side])
plt.gray()
plt.show()
