palabra1 = input('Ingrese una palabra 1: ')

palabra2 = input('Ingrese una palabra 2: ')

if(len(palabra1) == len(palabra2)):
    

    p1 = list(palabra1)
    p2 = list(palabra2)

    aux = []

    for i in range(len(p1)):
        letra = p1[i]
        
        for j in range(len(p2)):
            if letra == p2[j]:
                aux+=[letra]
                #p2[j]=''
                break
    if aux == p1:
        print('Es un anagrama')
    else:
        print('No es un anagrama')
        
        
    print(aux)
else:
    print('No es posible formar un anagrama con esas palabras')
