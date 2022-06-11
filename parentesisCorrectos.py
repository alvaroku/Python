

def validar(cadena):
    cont = 0
    for i in cadena:
        if i == '(':
            cont+=1
        elif i == ')':
            cont-=1

    print("contador: ",cont)
    if cont == 0:
        return True
    else:
        return False

cadena = 'Hola(Mundo) este es mi (primer)programa'
cadena1 = '(Hola(Mundo) este es mi (primer)programa'


if validar(cadena1):
    print("Correcto")
else:
    print('Incorrecto')
    
