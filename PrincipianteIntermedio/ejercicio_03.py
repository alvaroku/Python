
res = 1
print('..................................')
print('Bienvenido a su calculadora básica')
print('..................................')

while res==1:
    print('Puede realzar las siguentes operaciones')
    print(' 1.Sumar dos números\n 2.Restar dos números\n 3.Multiplicar dos numeros\n 4.Dividir dos números')
    
    op = int(input('Ingrese el número de opción: '))
    print('..................................')
    
    if op == 1:
        n1 = float(input('Ingrese el primer número: '))
        n2 = float(input('Ingrese el segundo número: '))

        print(f'La suma de {n1} + {n2} es {n1+n2}')
        print('..................................')
        
    elif op == 2:
        n1 = float(input('Ingrese el primer número: '))
        n2 = float(input('Ingrese el segundo número: '))

        print(f'La resta de {n1} - {n2} es {n1-n2}')
        print('..................................')

    elif op == 3:
        n1 = float(input('Ingrese el primer número: '))
        n2 = float(input('Ingrese el segundo número: '))

        print(f'La multiplicación de {n1} * {n2} es {n1*n2}')
        print('..................................')

    elif op == 4:
        n1 = float(input('Ingrese el primer número: '))
        n2 = float(input('Ingrese el segundo número: '))
        while n2==0:
            n2 = float(input('Ingrese un número distinto de 0: '))
            

        print(f'La división de {n1} / {n2} es {n1/n2}')
        print('..................................')
        
    print('Desea realizar otra operación?')
    print(' 1.Sí\n 2.No')
    res = int(input('Ingres el número de opción: '))
    print('..................................')

print('Gracias por usar nuestra calculadora básica')
