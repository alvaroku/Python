#esta linea sirve para imprimir mensajes
print('Hola mundo')
#tipos de variables
edad=22
decimal = 1.5
texto = 'alvaro ku'
booleano = True
#imprimiendo variables
print("Edad: "+str(edad))
print("Decimal:",decimal)
print("Booleano:",booleano)

#cálculo del área de un rectángulo
#capturando datos del teclado
b  = float(input('Ingrese el valor de la base: '))
h = float(input('Ingrese el valor de la altura: '))
#realizando una operacion
area = (b*h)/2
#mostrar el resultado
print("el area es: ",area,"unidades cuadradas")

#cálculo del volumen de un cubo
#capturando datos del teclado
a  = float(input('Ingrese el valor del lado a: '))
b = float(input('Ingrese el valor del lado b: '))
c  = float(input('Ingrese el valor del lado c: '))
#realizando una operacion
volumen = a * b *c
#mostrar el resultado
print("El volmen es:",volumen)
input()