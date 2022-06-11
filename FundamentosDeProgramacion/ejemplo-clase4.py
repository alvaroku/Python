#recorrer variable de tipo texto como arreglo
s = "mi nombre es alvaro"
#sin indice
for letra in s:
    print(letra)
print("---------------")
#con indice
for iLetra in range(len(s)):
    print(s[iLetra])

print("---------------")
#recorrer arreglo con while
a = [1,4,5,3]
indice = 0
while indice < len(a):
    print(a[indice])
    indice+=1
print("---------------")
#llenado de un arreglo con datos del teclado
b = []
n = 5
for indice in range(n):
    b+=[int(input('ingrese un valor: '))]
print(b)
#filtrando los datos
#contador de positivos
contador_de_positivos = 0
for elemento in b:#con este ciclo recorremos cada elemento del arreglo b
    if elemento<3:
        print("es menor que 3")
    elif elemento > 3 and elemento < 10:
        print('esta en el rango de 3 y 10')
    else:
        print('otro caso')
    #esta condicion es independiente de las anteriores
    if elemento > 0:
        contador_de_positivos += 1
print('total de positivos:',contador_de_positivos)
print("---------------")
#suma de los elementos de un arreglo
c = [1,5,7,4,6,4,5]
suma = 0
for numero in c:
    suma+=numero
promedio = suma/len(c)
print(c)
print("la suma es: ",suma)
print("el promedio es: ",promedio)
print('---------------')
#llenando de ceros un arreglo bidimensional
columnas = 3
filas = 2
arregloBi = [
    [0 for i in range(columnas)]for j in range(filas)
    ]
print(arregloBi)
#capturar cada valor del arreglo bidimencional
for iFila in range(0,len(arregloBi)):#este ciclo recorre cada fila del arreglo
    print("Fila",(iFila+1))
    for iColumna in range(0,len(arregloBi[iFila])):#este recorre cada elemento de cada fila
       arregloBi[iFila][iColumna] = int(input('Ingrese un numero: '))
print(arregloBi)