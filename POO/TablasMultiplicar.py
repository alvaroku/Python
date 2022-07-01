
class Tabla:
    def CalcularMultiplicacion(self, numero1, numero2):
        return numero1*numero2

    def CalcularTabla(self):
        lista = []
        for i in range(1, 11):
            for j in range(1, 11):
                lista+=[[i,j,self.CalcularMultiplicacion(i,j)]]
        return lista
class PresentadorDeDatos:
    def ShowTitle(self,title):
        print("*"*(len(title)+4))
        print("| "+title+" |")
        print("*"*(len(title)+4))

    def ShowText(self,text):
        print(text)

class VisualizadorTablas:
    def __init__(self,prd):
        self.visualizadorDeDados = prd
    def Visualizar(self,tablas):
        cont=0
        for tabla in tablas:
            if cont == 10:
                cont=0
                self.visualizadorDeDados.ShowText("")
            cont+=1

            self.visualizadorDeDados.ShowText(f"{tabla[0]} x {tabla[1]} = {tabla[2]}")

class App:
    tabla = Tabla()
    prd = PresentadorDeDatos()
    vt = VisualizadorTablas(prd)

    def Run(self):
        self.prd.ShowTitle("Tablas de multiplicar")
        tablas = self.tabla.CalcularTabla()
        self.vt.Visualizar(tablas)

app = App()
app.Run()