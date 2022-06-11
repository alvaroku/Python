
def parametrosIndeterminados(*parametros):
    for parametro in parametros:
        print(parametro)

def sumar(num1=0,num2=0):
    print(num1+num2)

def siImportaElOrdenDeParametros(nombre,edad):
    print(f"hola {nombre} tu edad es {edad}")

def noImportaElOrdenDeParametros(nombre,edad):  
    print(f"hola {nombre} tu edad es {edad}")
def validarEdad(numero):
    while numero<18:
        numero = int(input('Por favor ingrese un número mayor a 18: '))
    return numero

def validarNumeroEntero(numero):
    while True:
        try:
            numero = int(numero)
            break
        except:
            print('Por favor ingrese un número entero: ')
            numero = input()
    return numero

def validarNumeroFlotante(numero):
    while True:
        try:
            numero = float(numero)
            break
        except:
            print('Por favor ingrese un número con decimal: ')
            numero = input()
    return numero

siImportaElOrdenDeParametros(21,"alvaro")
noImportaElOrdenDeParametros(edad=21,nombre="alvaro")
sumar(6,3)
parametrosIndeterminados("hola",32,[1,2,3])
bandera = True
while bandera:
    print("""-------------------
Menu
-------------------
1.Sumar
2.Restar
3.Salir""") 
    opcion = validarNumeroEntero(input('Ingrese una opcion: '))
    if(opcion == 1 ):
        print("Elegiste la opcion suma")
        #pedir numero1 y numero 2, validarlo con la funcion validarflotante
        #hacer operacion
        #mostrar resultado
    elif opcion == 2:
        print("Elegiste la opcion resta")
    elif opcion == 3:
        print("Saliendo del menu")
        bandera= not bandera
    else:
        print('Opcion no válida')

validarNumeroFlotante("4w")
validarNumeroEntero("r")