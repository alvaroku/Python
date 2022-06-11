import matplotlib
import matplotlib.pyplot as plt
import numpy as np
 

#Definimos una lista con paises como string
paises = ['Estados Unidos', 'España', 'Mexico', 'Rusia', 'Japon']
#Definimos una lista con ventas como entero
ventas = [25, 32, 34, 20, 25]
 
#Recuperamos un par de valores de la función ‘subplots’,
#esto nos ayudara a añadir diversas características a la gráfica.
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Ventas')
#Colocamos una etiqueta en el eje X
ax.set_xlabel('Países');
#Colocamos un titulo a la gráfica
ax.set_title('Cantidad de Ventas por Pais')

#Creamos la grafica de barras utilizando 'paises' como eje X
#y 'ventas' como eje y.
plt.bar(paises, ventas)
plt.savefig('barras_simple.png')
#Finalmente mostramos la grafica con el metodo show()
plt.show()
