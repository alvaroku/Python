
num = 20

if num<100:
    print('Número menor que 100')


n = int(input('Ingrese su edad: '))

if n<18:
    print('Es menor de edad')
else:
    print('Es mayor de edad')


if num > 10 and n > 18:
    print('Uso de and')
elif num < 10 or n <= 18:
    print('Uso de or')

if not(n==20):
    print('Uso de not')
