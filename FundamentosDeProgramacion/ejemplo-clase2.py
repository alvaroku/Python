numero =20

#operadores relacionales < > == != <= >=
#estructura selectiva simples
if numero == 10:
    print("es igual 10")
else:
    print("no es igual a 10")
#estructura selectiva simples
if numero >= 10:
    print("es mayor o igual a 10")
else:
    print("no es mayor o igual que 10")

#estructura selectiva multiples
if numero >10:
    if numero <16:
        print("el numero es mayor a 10 y menor que 16")
elif numero <5:
    print("El numero es menor que 5")
else:
    print("otro caso")    

#operadores logicos and or not
if numero > 1 and numero < 10:
    print("se cumplió el and")
else:
    print("no se cumplió el and")

if numero > 1 or numero < 10:
    print("se cumplió el or")
else:
    print("no se cumplió el or")

if not(numero == 10):
    print("usando not")
else:
    print("otro caso")

#ciclo while->mientras
while numero == 20:
    print("el numero sigue siendo 20")
    numero = int(input('ingrese un numero: '))
print("se terminó el while")

for contador in range(1,11):
    print(str(contador)+"x"+str(3)+"="+str(3*contador))