while True:
    palabra = input ('Ingrese una palabra: ')
    aux = ''
    cont = len(palabra)-1
    
    while cont>=0:
        aux+=palabra[cont]
        cont-=1

    if palabra == aux:
        print(f'La palabra {palabra} es capicúa')
        break
    else:
        print(f'La palabra {palabra} no capicúa')
        print ('Intente otra')
