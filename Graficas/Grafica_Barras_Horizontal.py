import matplotlib
import matplotlib.pyplot as plt
import numpy as np

lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
#Obtenemos una lista con las posiciones de cada lenguaje, ejemplo 0, 1, 2, 3.....
y_pos = np.arange(len(lenguajes))
 
#Ahora obtenemos la cantidad de usos de cada lenguaje
cantidad_usos = [10,8,6,4,2,1]
 
#Creamos la grafica pasando los valores en el eje X, Y, donde X = cantidad_usos y Y = lenguajes
plt.barh(lenguajes, cantidad_usos, align='center', alpha=0.5)
 
#añadimos una etiqueta en el eje X
plt.xlabel('Usuarios')
#Y una etiqueta superior
plt.title('Lenguajes Mas Usados En El Año')
plt.savefig('barras_horizontal.png')
plt.show()
