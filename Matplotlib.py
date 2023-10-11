# Importar las librerias necesarias

import math
import numpy as np
from matplotlib import pyplot as plt

#Generamos los datos para el grafico

# Funcion del Seno
x = np.array (range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y [i] = math.sin(x[i])
    
#Funcion del Coseno

x1 = np.array (range(500))*0.1
y1 = np.zeros(len(x1))
for j in range(len(x1)):
    y1 [j] = math.cos(x1[j])

# Funcion de Tangente

x2 = np.array (range(500))*0.1
y2 = np.zeros(len(x2))
for p in range(len(x2)):
    y2 [p] = math.tan(x2[p])

#Titulo ala grafica

plt.title('Representaciòn de Funciones')

# Nombres alas coordenadas

plt.xlabel('Coordenda X')
plt.ylabel('Coordenda Y')

#Creamos el grafico
plt.plot(x,y,'*',x1,y1, 'p', x2,y2,'yellow' )

# Creaciòn de Leyenda
plt.legend(['Seno','Coseno', 'Tangente'])

#Termina Area de grafica
plt.show()


