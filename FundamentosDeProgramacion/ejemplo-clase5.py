#libreria integrada de python 
import math
#modulo para sumar 2 numeros, con parámetros, pero sin return
def suma(numero1,numero2):
    resultado = numero1 + numero2
    print("resultado",resultado)

#modulo para sumar 2 numeros, con parámetros, pero con return
def suma1(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

#modulo sin parametros sin return
def saludo():
    print("Hola")

#con parametro sin return
def saludo2(mensaje):
    print(mensaje)   

def mostrarDatosDeUnaLista(arreglo):
    for elemento in arreglo:
        print(elemento,end=" ")
    print()

def validarEdad():
    edad = int(input('Ingrese un numero: '))
    while edad<18:
        edad = int(input('Ingrese un dato valido: '))
    return edad

#llamadas a las funciones
resultado = suma1(100,300)
print(resultado)
saludo2("buenas tardes")
saludo2("buenas noches")

lista = [1,32,5,3]
mostrarDatosDeUnaLista(lista)

mostrarDatosDeUnaLista([1,5,87,4])

edad = validarEdad()
print("edad validada ",edad)

#funcion de python
numero = 100
print(math.sqrt(numero))