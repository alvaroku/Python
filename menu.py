
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

def invertirnumero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

def listaNombres(lista):
    for i in lista:
        print(i,end=" ")

resp = 3   
if resp == 1:
    numero = int(input('Ingrese un numero: '))
    print(factorial(numero))
elif resp ==2:
    numero = int(input('Ingrese un numero: '))
    print(invertirnumero(numero))
elif resp == 3:
    lista = []
    numero = int(input('Cuantos nombres?: '))
    for i in range(numero):
        lista+=[input('Ingrese un nombre:')]
    listaNombres(lista)
    
elif resp == 4:
    pass
