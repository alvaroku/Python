#en esta parte se crea una clase llamada rectangulo
class Rectangulo:
  #se crea un constructor que recibe como parametreos los valores del ancho y alto del rectangulo
    def __init__(self, ancho, alto):
      #aqui se define los valores de los atributos de la clase
        self.ancho = ancho
        self.alto = alto
    #este es un metodo que calcula y retorna el área del rectangulo, en base a su ancho y alto
    def area(self):
      #calcula el area, y lo guarda en una variable 
        resultado = self.ancho * self.alto
        #regresa el valor del area
        return resultado
    #metodo que calcula y retorna el perimetro del rectangulo en base a su ancho y alto
    def perimetro(self):
      #reliza la operacion para calcular el perimetro y lo guarda en una variable
        resultado = 2 * (self.ancho + self.alto)
        #retorna el valor del perimetro
        return resultado
#aqui se crea un objeto de la clase rectangulo, enviandole como parametros los valores que tendrá cada uno de sus atributos
r = Rectangulo(10, 7)
#llama al método area, e imprime el valor retornado
print('Área del rectángulo: %.2f' % r.area())
#llama al método perimetro, e imprime el valor retornado
print('Perímetro del rectángulo: %.2f' % r.perimetro())

#de manera general, el programa crea un objeto llamado rectangulo, el cual tiene como atributos el ancho y el alto
#y en base a sus atributos el programa usa sus metodos para mostrar en pantalla tanto el área como el perímetro
