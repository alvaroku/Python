#definir un arreglo unidimensional
lista = [5,10,"texto",12,6,True,False]
#acceder a sus elementos
print(lista[0])
print(lista[2])
#contar elementos del arreglo
print(len(lista))
#agregar elementos
lista+=["alvaro"]
print(lista)
lista.append("jose")
print(lista)
#eliminar elementos
#me devuleve el ultimo elemento del arreglo y lo elimina
print(lista.pop())
print(lista)
#tambien se puede usar con un indice
print(lista.pop(0))
print(lista)
#remove elimina el elemento por valor
lista.remove('texto')
print(lista)
#recorrer arreglo
print("imprimiendo elementos del arreglo manera 1")
for elemento in lista:
    print(elemento)
print("imprimiendo elementos del arreglo manera 2")

for indice in range(0,len(lista)):
    print(lista[indice])

#definir un arreglo bidimensional
print("arreglo multidimensional")
matriz = [
    [1,2,3,4],
    [1,2,100,4]
]
for fila in matriz:
    print("fila")
    for columna in fila:
        print(columna)

for iFila in range(0,len(matriz)):
    print("Fila",(iFila+1))
    for iColumna in range(0,len(matriz[iFila])):
        print(matriz[iFila][iColumna])