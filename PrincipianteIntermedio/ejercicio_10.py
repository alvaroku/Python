import random

def matriz(n):
    mat = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux+=[random.randint(0,10)]
        mat+=[aux]
    return mat
    
 
esPrima = False
A = matriz(3)
print('Matriz: ')
for i in A:
    print(i)

for i in range(len(A)):
    sumaFila=0
    for j in range(len(A)):
        sumaFila+=A[i][j]

    #print(sumaFila)
    for k in range(len(A)):
        sumaCol=0
        for l in range(len(A)):
            sumaCol+=A[l][k]

        #print(sumaCol)
        if sumaFila==sumaCol:
            esPrima=True
            break


if esPrima:
    print('Es prima')
else:
    print('No es prima')
