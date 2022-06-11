#misma posicion Toros
#en lista Vacas
import random
#num1 = str(random.randrange(111111,999999))
num1='300608'
#print(num1)

lista = list(num1)
print(lista)
num2 = input('Serie: ')
#print(num2)

lista2 = list(num2)
#print(lista2)

#print(lista)
print(lista2)

toros = 0
vacas = 0
posToros=[]
for i in range(len(lista)):
    if lista[i] == lista2[i]:
        toros+= 1
        posToros+=[i]


print('mismas posiciones',posToros)        
for i in range(len(lista)):
    if (lista[i] in lista2) and (i not in posToros):
        vacas+=1
                   
       

       
print('Toros: ',toros)
print('Vacas: ',vacas)



#
