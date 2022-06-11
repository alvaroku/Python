import pandas as pd

 

datos = []

while True:
    print('Menú')
    print('1.Agregar\n2.Ver Registros de la agenda\n3.Salir')

    o = input('Ingrese una opción:')
    print('..........................')
    if o == '1':
        nombre = input('Ingresar nombre: ')
        direc = input('Ingresar dirección: ')
        ciudad = input('Ingresar cuidad: ')
        cPostal = input('Ingresar código postal: ')
        tel = input('Ingresar télefono: ')
        edad = input('Ingresar edad: ')

        columnas = [nombre,direc,ciudad,cPostal,tel,edad]

        datos+=[columnas]
        df = pd.DataFrame(datos, columns=["nombre","direccion",'ciudad','codigo postal',
                                      'telefono','edad'])
        df.to_csv('archivo.csv', index=False)


    elif o == '2':
        
        df = pd.read_csv('archivo.csv')

        print("nombre\t","direccion\t",'ciudad','\tcodigo postal','telefono\t','edad')
        for i in range(len(df)):
            print(df['nombre'][i],'\t',df['direccion'][i],'\t',df['ciudad'][i],'\t',df['codigo postal'][i],'\t',df['telefono'][i],'\t',df['edad'][i])
        print('..........................')
    else:
        break
    
        
        
    
