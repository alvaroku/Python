import random

def matriz(n):
    mat = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux+=[random.randint(0,10)]
        mat+=[aux]
    return mat
    
def multiplicar(a,num,n):
    mat = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux+=[a[i][j]*num]
        mat+=[aux]
    return mat
    
A = matriz(3)

numero = float(input('Ingrese un número: '))
print('Matriz : ',A)
 

print(f'Resultado de A*{numero}')
print(multiplicar(A,numero,len(A)))
