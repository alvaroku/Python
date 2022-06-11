class Empleado():
    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.sueldo = float(input('Ingrese su sueldo: '))

    def imprimirDatos(self):
        print(f'Nombre del empleado: {self.nombre}\nSueldo {self.sueldo}$')

    def comprobarImpuestos(self):
        if self.sueldo>3000:
            print('Paga impuestos')
        else:
            print('No paga impuestos')


while True:
    e = Empleado()
    print()
    e.imprimirDatos()
    print()
    e.comprobarImpuestos()
    print()
    
    o = int(input('Ingresar otro empleado?\n 1.Sí\n 2.No\nIngrese una opción: '))
    if o != 1:
        break
    print('...........................')
    
