lista = [1,2,3,4,5]

for i in lista:
    print(i)

print()

for i in range(len(lista)):
    print(lista[i])

for i in range(len(lista)):
    print(lista[i],end = " ")

print()

print(lista)

print()

lista[0] = True

print(lista)

print()

print('Tamaño de lista', len(lista))

print()

lista.remove(4)

print(lista)
