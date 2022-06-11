import random
m = 0
n = 0
arreglo = []
while (True):
  m = int(input('Numero 1 (del 3 al 6): '))
  if m>0 and m>=3 and m<=6:
    break

while (True):
  n = int(input('Numero 2 (del 3 al 6): '))
  if n>0 and n>=3 and n<=6:
    break
 
 #llenar
for i in range(m):
  aux = []
  for j in range(n):
    aux+=[random.randint(0,9)]
  arreglo+=[aux]

#imprime arreglo
for i in arreglo:
  print(i)

#suma de filas
for i in range(m):
  print('Suma de fila',i+1)
  suma = 0
  for j in range(n):
    suma+=arreglo[i][j]
  print(suma)
    
#promedio de columnas
for i in range(n):
  print('Promedio columna',i+1)
  suma = 0
  for j in range(m):
    suma+=arreglo[j][i]
  print(suma/m)