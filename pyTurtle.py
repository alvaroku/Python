#Fromas Basicas con la tortuga de python

import turtle


def rectangulo():
    C = 5
    a = angulo/4
    for i in range(2):
        t.forward(L)
        t.left(a)
        t.forward(C)
        t.left(a)

def cuadrado():
    a = angulo/4
    for i in range(4):
        t.forward(L)
        t.left(a)

def triangulo():
    a = 360/3
    for i in range(3):
        t.forward(L)
        t.left(a)

def poligono():
    l = 5
    a = 360/l
    for i in range(l):
        t.forward(L)
        t.left(a)

def circulo():
    a = angulo/360
    for i in range(360):
        t.forward(2)
        t.left(a)
    

#definir grados
angulo = 360
L = 50

#crear tortuga
t = turtle.Turtle()
t.shape('turtle')
t.speed(100)

#llamar funciones

for i in range(35):
    triangulo()
    t.left(10)

for i in range(35):
    poligono()
    t.left(10)

for i in range(36):
    L = 100
    cuadrado()
    t.left(10)

for i in range(36):
    L = 200
    rectangulo()
    t.left(10)

#for i in range(10):
 #   circulo()
  #  t.left(10)
        


'''or i in range(1):
    rectangulo()
    cuadrado()
    triangulo()
    poligono()
    L+=20'''

