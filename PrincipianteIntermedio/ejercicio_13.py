def agregar(nombre,apellido,telefono):
    file = open('agenda.txt','a')
    file.write(nombre+','+apellido+','+telefono+'\n')
    file.close()
        
def buscarTelefono(nombre,apellido):
    n = ''
    file = open('agenda.txt','r')
    for linea in file:
        linea = linea.replace('\n','').split(',')
        if linea[0]==nombre and linea[1]==apellido:
            n = linea[2]
    file.close()

    return n
    
 
def borrar(nombre,apellido):
    borrado = False
    file = open('agenda.txt','r')
 
    lista = []
    for linea in file:
        linea = linea.replace("\n",'')
        lista+=[linea.split(',')]
        #print(linea)     
    #print(lista)
    file.close()

    for i in range(len(lista)):
        if lista[i][0] == nombre and lista[i][1]==apellido:
            lista.remove(lista[i])
            borrado = True
            break
            
    file = open('agenda.txt','w')
    for i in lista:
        file.write(f'{i[0]},{i[1]},{i[2]}\n')
 
    file.close()

    return borrado
    
    
def verContactos():
    file = open('agenda.txt','r')
    print('Contactos')
    for linea in file:
        linea = linea.replace('\n','').split(',')
        print(linea[0],'\t',linea[1],'\t',linea[2])      
    file.close()

while True:
    print('---------------------------\nOpciones')
    print(' 1.Agregar Contacto\n 2.Buscar télefono con nombre y apellido\n 3.Borrar entrada con nombre y apellido\n 4.Ver contactos\n 5.Salir')
    print('---------------------------')
    
    o = int (input('Ingrese una opción:'))
    print('.............................')
    
    if o == 1:
        agregar(input('Nombre: '),input('Apellido: '),input('Télefono: '))
        print('Contacto agregado')
    elif o == 2:
        telefono = buscarTelefono(input('Nombre: '),input('Apellido: '))
        if len(telefono)==0:
            print('No se pudo encontrar ningun télefono con esos datos')
        else:
            print('El télefono encontrado es',telefono)
    elif o == 3:
        if(borrar(input('Nombre: '),input('Apellido: '))):
            print('Contacto borrado')
        else:
            print('No se encontro ningun contacto con esos datos')
    elif o == 4:
        verContactos()
    else:
        break

    print('.............................')
    





    
    
