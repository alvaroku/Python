#ABEL MOSALI MENDEZ LOPEZ
from tkinter import *

class PyApp(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.Vi = StringVar()
        self.R2 = StringVar()
        self.R1 = StringVar()

        self.resultado = StringVar()

        self.EtiquetaTitulo = Label(self, font=(
            "Arial", 20), text="Divisor de Tensión")
        self.EtiquetaTitulo.grid(row=2, column=0)

        self.entradaVi = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.Vi)
        self.entradaVi.insert(0, "0")
        self.entradaVi.grid(row=6, column=0)

        self.EtiquetaEntradaVi = Label(
            self, font=("Arial", 15), text="V")
        self.EtiquetaEntradaVi.grid(row=6, column=1)
        #########################

        self.entradaR2 = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.R2)
        self.entradaR2.insert(0, "0")
        self.entradaR2.grid(row=8, column=0)

        self.EtiquetaEntradaR2 = Label(
            self, font=("Arial", 15), text="kΩ")
        self.EtiquetaEntradaR2.grid(row=8, column=1)
        #############################


        self.entradaR1 = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.R1)
        self.entradaR1.insert(0, "0")
        self.entradaR1.grid(row=10, column=0)

        self.EtiquetaEntradaR1 = Label(
            self, font=("Arial", 15), text="kΩ")
        self.EtiquetaEntradaR1.grid(row=10, column=1)
        ###############################


        self.ceButton = Button(self, font=("Arial", 12),
                               text="Calcular", command=self.Calcular, width=10)
        self.ceButton.grid(row=13, column=0)

        self.EtiquetaResultado = Label(self, font=(
            "Arial", 24), textvariable=self.resultado)
        self.EtiquetaResultado.grid(row=15, column=0)

    def Calcular(self):
        vi = float(self.entradaVi.get())
        r2 = float(self.entradaR2.get())
        r1 = float(self.entradaR1.get()) 
        #Vi/(R1+R2) x R2
        Vo =   vi/(r1+r2)*r2
        Vo = round(Vo,3)
        Vo = str(Vo)+"V"
        self.resultado.set(Vo)

App = Tk()
App.title("Divisor de Tensión")
App.geometry("300x250")

root = PyApp(App).grid()

App.mainloop()
