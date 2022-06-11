
def mensaje():
    print('Bienvenido')
    
def mensaje2(mensaje):
    print(mensaje)

def add(lista, dato):
    lista+=[dato]

def mostrar(lista):
    for i in lista:
        print(i)

        
lista1 = []
lista2 = []

mensaje()
mensaje2('Uso de funciones')

add(lista1,6)
add(lista1,True)
add(lista1,'Hola') 

mostrar(lista1)

 

 
 
