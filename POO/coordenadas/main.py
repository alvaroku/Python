import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def info(self):
        print('coordenadas: ({0},{1})'.format(self.getX(), self.getY()))


def distancia(p1, p2):
    return math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)


if __name__ == '__main__':
    p1 = Punto(2, 9)
    p2 = Punto(3, 2)
    print('Punto 1')
    p1.info()
    print('Punto 2')
    p2.info()
    print('Distancia: {0}'.format(distancia(p1,p2)))
