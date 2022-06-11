#!/usr/bin/env python
# -*- coding: utf-8 -*-

#aqui se importa la libreria numpy, para poder aplicar sus funciones en las matrices
import numpy as np
#se importa la libreria os para realizar operaciones dependiente del Sistema Operativo 
import os

# en esta parte se hacen condiciones para comparar el nombre sel sistema operativo,
#y asi poder definir el valor de la variable var que es el nombre de la funcion de limpieza de la consola
if os.name == "posix":
    #si la condicion anterior se cumple la variable var es igual a clear
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    # en caso de que cualquiera de las 3 condiciones de cumplan el valor de ver será cls
    var = "cls"

#esta es una funcion para validar que el numero recibido como parametro sea un entero 
def OKI(n):
    #se usa try except para controlar el error y asi el programa no se detenga
    try:
        #intenta convertir el valor a entero
        n=int(n)
    except:
        #si falla al convertir, esta funcion se vuelve a llamar a sí misma para repetir el proceso
        n=OKI(input("Caracter no valido: "))
    #se retorna el valor convertido a entero
    return n

#funcion para validar un valor de tipo float
def OK(n):
    try:
        #intenta convertirel valor a un valor flotante
        n=float(n)
    except:
        # en caso de fallar lo anreior, esta funcion se vuelva a llamar a sí misma, y se repite el proceso
        n=OK(input("Caracter no valido: "))
    #se retorna el valor convertido a un valor flotante
    return n

#funcion que valida que el valor del parametro recibido sea una 's' o una 'n'
def ns(c):
    # ciclo que se ejecuta mientras el valor ingresado ses diferente de una 's' y una 'n'
    while c!=("s") and c!=("n"):
        #imprime un caracter
        print(chr(7));
        #vuelve a pedir el dato
        c=input("Escribe solo \'n\' o \'s\' según su opción: ").lower()
    #retorna el valor de c
    return(c)

#funcion que valida que el valor recibido como parametro sea una 'N' o una 'M'
def val(tp):
    #ciclo que se repite meintras el valor ingresado sea diferente de 'N' y 'N'
    while tp!="N" and tp!="M":
        #vuelve a capturar el dato
        tp=input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ").upper()
    #retorna el valor
    return tp
 
#FUNCIÓN DE TIPO DE DATO
def dato():
    #llama a la funcion val enviandole el valor capturado
    tipo_dato=val(input("Tipo de dato: ").upper())
    #si el valor es 'M'
    if tipo_dato=="M":
        #llama a la funcion crea_matriz y  le envia los valores fil y col
        matr=crea_matriz(fil,col)
    else:
        #sino llama a la funcion OK
        matr=OK(input("Introduce número: "))
    # en base a las condiciones, retorna una matriz o un valor numerico
    return matr
 
#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col):
    #imprime un salto de linea
    print("")
    #inicializa las variables en -1
    f=-1;c=-1
    #crea un vector vacio para las filas
    e_fil=[]
    #ciclo que recorre el rango de las filas
    for f in range(fil):
        #crea un vector vacio para las columnas
        e_col=[]
        #incrementa f
        f+=1
        #ciclo que recorre el rango de las columnas
        for c in range(col):
            #increnta c
            c+=1
            #captura un numero,y lo valida con la funcion OK
            valor=OK(input('Introduzca el componente (%d,%d): '%(f,c)))
            #agrega el dato al vector de columnas
            e_col.append(valor)
        #agrega el vector de columnas al vector de fulas
        e_fil.append(e_col)
        #usa la funcion de numpy para crear uns mstriz con la lista bidimensional e_fil
        matri=np.array(e_fil,float)
    #retorna la matriz
    return matri

#ciclo para mostrar el menu de opciones
while True:
    #se imprimen las opciones
    print("          CALCULADORA DE MATRICES          ")
    print("""***********TABLA DE OPERADORES***********
*****************************************
SUMA                           OPERADOR "+"
RESTA                          OPERADOR "-"
MULTIPLICACIÓN                 OPERADOR "*"
FINALIZAR CALCULO              OPERADOR "C"
DATO MATRIZ                    OPERANDO "M"
DATO NÚMERO                    OPERANDO "N"
*****************************************
*******************************************\n""")
    #captura la variable fil, validandola con al funcion OKI
    fil=OKI(input("Indique número de filas: "))
    #captura la variable col, validandola con al funcion OKI
    col=OKI(input("Indique número de columnas: "))
    #en e guarda el valor de fil
    e=fil
    #inicializa f y c en -1
    f=-1;c=-1
    #crea una matriz con la funcion crea_matriz de tamaño fil*col
    acum=crea_matriz(fil,col)
    #imprime la matriz
    print("\nRESULTADO")
    print(acum,"\n")
    #ciclo para la parte de las operaciones
    while True:
        #captura el operador
        oper=input("Introduzca operador: ")
        #ciclo que se repite mientras la variable oper sea diferente de un +-* y C
        while oper!="+" and oper!="-" and oper!="*" and oper!="C":
            #vuelve a capturar el operador hasta que sea valido
            oper=input("Introduzca un operador válido: ")
        #si es +    
        if oper=="+":
            #llama a la funcion dato y el valor retornado ya sea una matroz o un valor numerico lo guarda en matr
            matr=dato()
            #hace la operacion de suma
            acum=acum+matr
        #si es un -
        elif oper=="-":
            #llama a la funcion dato y el valor retornado ya sea una matroz o un valor numerico lo guarda en matr
            matr=dato()
            #realiza la operacion de resta
            acum=acum-matr
        #si es un *
        elif oper=="*":
            #llama a la funcion val para validar el tipo de dato
            tipo_dato=val(input("Tipo de dato: ").upper())
            #su el tipo de dato es 'M'
            if tipo_dato=="M":
                #guarda el calor de col en fil
                fil=col
                #captura el numero de columnas y lo valida con la funcion OKI
                col=OKI(input("Introduce número de columnas: "))
                #crea una matriz fil*col
                matr=crea_matriz(fil,col)
                #llama ala funcion del producto de puntos de numpy, y el valor retornado lo guarda en acum
                acum=np.dot(acum,matr)
                #guarda e en fil
                fil=e
            #sino 
            else:
                #captura un numero
                matr=OK(input("Introduce número: "))
                #hace la operacion de multiplicacion de una matriz po un numero
                acum=acum*matr
        #si la opcion es diferente de 'C'
        if oper!="C":
            #muestra la matriz resultante
            print("\nRESULTADO")
            print(acum,"\n")
        #sino es niguna opcion
        else:
            #rompe el ciclo y continua con la flujo del programa
            break
    #captura una opcion y la valida con la  funcion ns 
    conti=ns(input("¿Reiniciar cálculos?: ").lower())
    #si es n 
    if conti=="n":
        #rompe el ciclo y termina la ejecucion 
        break
    #continua la ejecicion y se repite todo el proceso
    #reinicia la variable matr
    matr=0
    #limpia la consola
    os.system(var)


# en general el programa cuenta con un menu de operaciones de mtrices, al inicio se crea una matriz de fil*col, se intrducen sus elementos
#se puede realizar operaciones como suma, resta y multiplicacion, ya sea con otra matriz o con un valor numerico
#en el menu contamos con la opcion de repetir calculos con nuevas matrices o tambien podemos finalizar para cerrar el programa.
