# Importamos las librerias necesarias
import math
import numpy as np
from matplotlib import pyplot as plt

# Funcion de Seno

x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Funcion de Coseno
x_2 = np.array(range(500))*0.1
y_2 = np.zeros(len(x_2))
for j in range(len(x_2)):
    y_2[j] = math.cos(x_2[j])

# Funcion de Tangente

x_3 = np.array (range(500))*0.1
y_3 = np.zeros(len(x_3))
for p in range(len(x_3)):
    y_3 [p] = math.tan(x_3[p])


# Creamos el gráfico
#Numero de filas
#Numero de columnas
plt.subplot(221)
plt.plot(x,y,'yellow')
plt.xlabel('Coordenda X')
plt.ylabel('Coordenda Y')
plt.title('Representacion del grafico Seno')

plt.subplot(222)
plt.plot(x_2,y_2,'p')
plt.xlabel('Coordenda X')
plt.ylabel('Coordenda Y')
plt.title('Representacion del grafico Coseno')

plt.subplot(223)
plt.plot(x_3,y_3,'--')
plt.xlabel('Coordenda X')
plt.ylabel('Coordenda Y')
plt.title('Representacion del grafico Tangente')

plt.show()
