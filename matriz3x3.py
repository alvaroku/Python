from random import randint
fil = 3
col = 3
a = [[randint(1,100)for i in range(fil)]for j in range(col)]

for i in a:
    print(i)

for f in range(fil):
    for c in range(col):
        if c == f:
            print(a[f][c],end=" ")
print()

aux = []
for f in range(fil):
    for c in range(col):
        aux+=[a[f][c]]
print(aux)

for i in range(1,len(aux)):
    for j in range(0,len(aux)-i):
        if(aux[j+1] < aux[j]):
            temp=aux[j];
            aux[j]=aux[j+1];
            aux[j+1]=temp;
print(aux)
input()
