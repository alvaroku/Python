from asyncio.windows_events import NULL


class Auto:
    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def info(self):
        return f'{self.color} {self.ruedas}'
        
def catalogar(listaAutos,ruedas=NULL):
    if ruedas:
        cont = 0
        for i in listaAutos:
            if ruedas == i.ruedas:
                print(f'Nombre de clase: {type(i).__name__}')
                print(f'Atributos {i.info()}')
                cont+=1
        print(f'Se han encontrado {cont} vehículos con {ruedas}')
    else:
        for i in listaAutos:
            print(f'Nombre de clase: {type(i).__name__}')
            print(f'Atributos {i.info()}')

    
a1 = Auto("rojo",4)
a2 = Auto("rojo",6)
a3 = Auto("rojo",4)

lista = [a1,a2,a3]

catalogar(lista,0)