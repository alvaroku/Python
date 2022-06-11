carrito = {}
cont = 0

while True:
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    
    articulo = {'nombre':nombre,'precio':precio}

    carrito[f'art{cont}'] = articulo
    
    o = int(input('Agregar más productos?\n 1.Sí\n 2.No\nIngrese una opción: '))
    if o!=1:
        break
    
    cont+=1
    
print('')
total = 0
print('Lista de la compra')
print('-----------------------------')
for key in carrito:
    print(carrito[key]['nombre'],'\t',carrito[key]['precio'])
    total+=carrito[key]['precio']
    print('-----------------------------')


print('Total','\t',total)
    
    
