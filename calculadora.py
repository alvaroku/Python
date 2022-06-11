class Calculadora():
    
    def __init__(self):
        print("ESTA ES UNA CALCULADORA BÁSICA")

    def suma(self,num1,num2):
        return num1+num2

    def resta(self,num1,num2):
        return num1-num2

    def multiplicacion(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        return num1/num2

    def cuadrado(self,num1):
        return num1**2

    def nPotencia(self,num1,n):
        return num1**n

    def raizCuadrada(self,num1):
        return num1**(1/2)

    def nRaiz(self,num1,n):
        return num1**(1/n)
         

c = Calculadora()
b1 = True
b2 = True
print('''------------------------------
-           MENÚ             -
------------------------------
1.SUMA
2.RESTA
3.MULTIPLICACIÓN
4.DIVISIÓN
5.ELEVAR AL CUADRADO
6.N POTENCIA
7.RAÍZ CUADRADA
8.N RAÍZ
9.SALIR
------------------------------''')
while b1:
    while b2:
        o = input('Ingrese una opción: ')
        try:
            o = int(o)
            b2=False
        except:
            print('Ingrese un número')

        if o == 1:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            print('{0}+{1}={2}'.format(num1,num2,c.suma(num1,num2)))
            b2=True
        else:
            b1=False
    

