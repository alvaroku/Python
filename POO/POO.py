class Humano: 
    def __init__(self,nom,edad):
        print('Soy un humano')
        self.nombre = nom
        self.edad = edad   
    def setNombre(self,nom):
        self.nombre = nom
    def getNombre(self):
        return self.nombre
    def setEdad(self,edad):
        self.edad = edad
    def getEdad(self):
        return self.edad
    def hablar(self):
        print('Tengo ',getEdad(),' años')

class ISC(Humano):
    def __init__(self,nom,edad,leng):
        super().__init__(nom,edad)
        self.lenguaje = leng
        print('Soy un ISC')
    def setLenguaje(self,leng):
        self.lenguaje = leng
    def getLenguaje(self):
        return self.lenguaje
    def hablar(self,mensaje):
        print(mensaje)      
ingeniero = ISC('Pepe Rodriguez',20,'Python')
print(ingeniero.getNombre())
print(ingeniero.getEdad())
print(ingeniero.getLenguaje())
ingeniero.hablar('Soy desarrollador android')


