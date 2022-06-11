A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
     'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
C = [1,2,3,4,5,6,7,8,9,0]
D = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡']

seleccion = False
concatenacion = False
d = False

identificador = '(A|B)CCCD'

cadena = "A123#"
     

print(identificador)
print (cadena)

if len(cadena) == 5:
    
    if cadena[0]in A or cadena[0] in B:
        seleccion = True
    else:
        print('Debe tener un caracter del alfabeto A ó B en la posición 1')

    try:

        int(cadena[1])in C and int(cadena[2])in C and int(cadena[3])
        concatenacion = True
    except:
        print('Debe tener un caracter del alfabeto C en la posición 1 y 2')

    if cadena[4] in D:
        d = True
    else:
        print('Debe tener al final un caracter del alfabeto D')
        
    print(seleccion,concatenacion,d)
    if (seleccion == True and concatenacion== True and d==True):
        print('Correcto')
