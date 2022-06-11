#simulacion de lanzar n veces 2 dados, mostrar cuantas veces los 2 tuvieron
#el mismo resultado
from random import randint
n = int(input('Cuántas veces: '))

cont=0
for i in range(n):
    d1 = randint(1,6)
    d2 = randint(1,6)

    if d1 == d2:
        cont+=1
        print(d1,d2,cont)
    

print('Total de repeticiones: ',cont)
