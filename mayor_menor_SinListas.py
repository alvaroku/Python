n = int(input("Cúantos numeros: "))

mayor = 0
menor = 0
 
for i in range(0,n):
    numero = int(input("Ingrese un numero: "))

    if i == 0 :
        mayor = numero
        menor = numero
    
    if numero>mayor:
        mayor = numero

    if numero<menor:
        menor = numero
 
print("El mayor es: ", mayor)    
print("El menor es: ", menor)
