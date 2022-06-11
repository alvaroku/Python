import random

def matriz(n):
    mat = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux+=[random.randint(0,10)]
        mat+=[aux]
    return mat
    
def restar(a,b):
    mat = []
    for i in range(3):
        for j in range(3):
            mat+=[ A[i][j] - B[i][j] ]
      
    return mat
    
A = matriz(3)
B = matriz(3)

print('Matriz A: ',A)
print('Matriz B: ',B)

print('Resultado de A-B')
print(restar(A,B))
