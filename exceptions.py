import sys

try:
    n = int (input ('Ingrese un número: '))
except:
    print('Por favor ingrese un número')


while True:
    try:
        n = int (input ('Ingrese un número: '))
        break
    except ValueError:
        print('Por favor ingrese un número')
        print("Unexpected error:", sys.exc_info()[0])
