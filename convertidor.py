
def conversion(n):
    
    if n > 1:
        
        conversion(n // 2)
        
    print(n % 2, end='')
    if n%2==1:
        lista.append(1)

while True:           
    lista = []
    nbr = int(input("Decimal: "))
    conversion(nbr)
    print()
    print(lista)
