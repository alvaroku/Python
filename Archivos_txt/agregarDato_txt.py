#a si no existe, crea el archivo
file = open('datos.txt','a')
file.write('\nLinea 11\n')
file.write('Linea 12')

file.close()

file = open('datos.txt','r')
print(file.read())
file.close()
