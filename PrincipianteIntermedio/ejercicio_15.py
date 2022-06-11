class Operaciones:
    def __init__(self):
        self.numero1 = int(input('Ingrese el primer número: '))
        self.numero2 = int(input('Ingrese el segundo número: '))

    def suma(self):
        print(f'{self.numero1} + {self.numero2} = {self.numero1+self.numero2}')
    def resta(self):
        print(f'{self.numero1} - {self.numero2} = {self.numero1-self.numero2}')
    def multiplicacion(self):
        print(f'{self.numero1} * {self.numero2} = {self.numero1*self.numero2}')

    def dividir(self):
        while self.numero2 == 0:
            print(f'No se puede dividir por {self.numero2}')
            self.numero2 = int(input(f'Igrese un número diferente de {self.numero2}: '))
        print(f'{self.numero1} / {self.numero2} = {self.numero1/self.numero2}')
        
        
while True:

    op = Operaciones()

    op.suma()
    op.resta()
    op.multiplicacion()
    op.dividir()
    
    o = int(input('Repetir proceso? \n 1.Sí\n 2.No\nIngrese una opción: '))
    if o != 1:
        break
    print('...........................')
    

