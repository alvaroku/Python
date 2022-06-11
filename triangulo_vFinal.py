from itertools import combinations#libreria para obtener combinaicones

def combinar(li,r):#recibe una lista y el numero de elementos de la combinacion
    combinaciones = list(combinations(li,r))#enlista las combinaciones
    return combinaciones#retorna la lista de combinaciones

def validar(n):
    while True:
        try:
            n = int(n)
            break
        except:
            n = input('Ingrese un número ')
    return n

li = []
liSi=[]
liNo=[]
liPer = []

while True:
    n = validar(input('Numero de datos para ingresar? '))
    if n >2:
        break

for i in range(n):
    li+=[validar(input('Ingrese un número '))]
    
print('------------------------')
print('Lista: ',li)
print('------------------------')

Licom = combinar(li,3)
   
print('Posibles combinaciones: ',Licom)
print('------------------------')

for sub in Licom:
    a=sub[0]
    b=sub[1]
    c=sub[2]
    #print(sub)
    if a==0 or b==0 or c==0:
        liNo+=[sub]
        
    elif ((a+b)>c) and ((a+c)>b) and ((b+c)>a)and( ((a-b)<c) and ((a-c)<b) and ((b-c)<a)):
        liSi+=[sub]
    else:
        liNo+=[sub]

if len(liNo)>0:
    print('No pueden formar triangulos: ',liNo)
    print('------------------------')
  


if len(liSi)>0:
    print('Si pueden formar triangulos: ',liSi)
    print('------------------------')
    for co in liSi:
        per = 0
    #print(i)
        for e in co:
        #print(e)
            per+=e
        liPer+=[per]
    print('Lista de perímetros',liPer)
    print('------------------------')
    mayor = max(liPer)

    posMayor = liPer.index(mayor)

    print()
    print('*************************************')
    print('Triángulo con mayor perimetro: ',liSi[posMayor])

    print('Su perímetro es: ',mayor)
    print('*************************************')
else:
    print('No hay triangulos')

        

