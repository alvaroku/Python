#ABEL MOSALI MENDEZ LOPEZ

from tkinter import *
from tkinter import messagebox

class PyApp(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.masa = StringVar()
        self.aceleracion = StringVar()
        self.fuerza = StringVar()
        self.opcion = StringVar()
        self.opcion.set(0)

        self.resultado = StringVar()

        self.EtiquetaTitulo = Label(self, font=(
            "Arial", 20), text="Segunda Ley Newton")
        self.EtiquetaTitulo.grid(row=2, column=0)

        values = {
            "Fuerza": "1",
            "Masa": "2",
            "Aceleración": "3"
        }
        c = 1
        for (text, value) in values.items():
            r = Radiobutton(self.master, text=text,
                            variable=self.opcion, value=value)
            r.grid(row=1, column=c)
            c += 1

        self.EtiquetaEntradaMasa = Label(self, font=("Arial", 15), text="Masa")
        self.EtiquetaEntradaMasa.grid(row=5, column=0)

        self.entradaMasa = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.masa)
        self.entradaMasa.insert(0, "0")
        self.entradaMasa.grid(row=6, column=0)

        self.EtiquetaEntradaUnidadMasa = Label(
            self, font=("Arial", 15), text="Kg")
        self.EtiquetaEntradaUnidadMasa.grid(row=6, column=1)
        #########################

        self.EtiquetaEntradaAceleracion = Label(
            self, font=("Arial", 15), text="Aceleración")
        self.EtiquetaEntradaAceleracion.grid(row=7, column=0)

        self.entradaAceleracion = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.aceleracion)
        self.entradaAceleracion.insert(0, "0")
        self.entradaAceleracion.grid(row=8, column=0)

        self.EtiquetaEntradaUnidadAceleracion = Label(
            self, font=("Arial", 15), text="m/s^2")
        self.EtiquetaEntradaUnidadAceleracion.grid(row=8, column=1)
        #############################

        self.EtiquetaEntradaFuerza = Label(
            self, font=("Arial", 15), text="Fuerza")
        self.EtiquetaEntradaFuerza.grid(row=9, column=0)

        self.entradaFuerza = Entry(self, font=(
            "Arial", 20), width=10, textvariable=self.fuerza)
        self.entradaFuerza.insert(0, "0")
        self.entradaFuerza.grid(row=10, column=0)

        self.EtiquetaEntradaUnidadFuerza = Label(
            self, font=("Arial", 15), text="N")
        self.EtiquetaEntradaUnidadFuerza.grid(row=10, column=1)

        self.ceButton = Button(self, font=("Arial", 12),
                               text="Calcular", command=self.Calcular, width=10)
        self.ceButton.grid(row=13, column=0)

        self.EtiquetaResultado = Label(self, font=(
            "Arial", 24), textvariable=self.resultado)
        self.EtiquetaResultado.grid(row=15, column=0)

    def Calcular(self):
        op = int(self.opcion.get())
        resu = ""

        if(op == 0):
            messagebox.showerror("Error", "Debe elegir una opción")
        elif(op == 1):
            resu = float(self.entradaMasa.get())*float(self.entradaAceleracion.get())
            resu = str(resu)+" N"
            self.resultado.set(resu)
        elif(op == 2):
            resu = float(self.entradaFuerza.get())/float(self.entradaAceleracion.get())
            resu = round(resu,3)
            resu = str(resu)+" Kg"
            self.resultado.set(resu)
        elif(op == 3):
            resu = float(self.entradaFuerza.get())/float(self.entradaMasa.get())
            resu = round(resu,3)
            resu = str(resu)+" m/s^2"
            self.resultado.set(resu)


App = Tk()
App.title("Segunda Ley Newton")
App.geometry("600x400")

root = PyApp(App).grid()

App.mainloop()
