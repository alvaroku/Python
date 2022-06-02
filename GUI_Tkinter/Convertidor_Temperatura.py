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
        self.temperatura = StringVar()
        self.opcion = StringVar()
        self.opcion.set(0)
        self.unidadDe = StringVar()
        self.resultado = StringVar()

        self.entrada = Entry(self, font=("Arial", 20),width=10, textvariable=self.temperatura)
        self.entrada.insert(0, "0")
        self.entrada.grid(row=2, column=0)

        self.EtiquetaUnidadDe = Label(self,font=("Arial", 20),textvariable=self.unidadDe)
        self.EtiquetaUnidadDe.grid(row=2, column=15)

        self.ceButton = Button(self, font=("Arial", 12), text="Calcular", command=self.Calcular,width=10)
        self.ceButton.grid(row=2, column=20)

        self.EtiquetaResultado = Label(self,font=("Arial", 24),textvariable=self.resultado)
        self.EtiquetaResultado.grid(row=2, column=30)

        values = {
            "Celsius a Fahrenheit" : "1",
            "Celsius a Kelvin" : "2",
            "Fahrenheit a Celsius" : "3",
            "Fahrenheit a Kelvin" : "4",
            "Kelvin a Celsius" : "5",
            "Kelvin a Fahrenheit" : "6"}
        c = 4
        for (text, value) in values.items():
            r = Radiobutton(self.master, text = text, variable =self.opcion,value = value)
            r.grid(row=c, column=0)
            c+=1
 
        
    
    def Calcular(self):
        if(self.temperatura.get()!=""):
            op = int(self.opcion.get())
            temp = float(self.temperatura.get())
            
            if(op==0):
                messagebox.showerror("Error","Debe seleccinar una opcion")
            elif(op==1):
                self.unidadDe.set("°C")
                resu = round((temp * 9/5) + 32,2)
                resu = str(resu)+ "°F"
                self.resultado.set(resu)
            elif(op==2):
                self.unidadDe.set("°C")
                resu = round( temp + 273.15,3)
                resu = str(resu)+ "°K"
                self.resultado.set(resu)
            elif(op==3):
                self.unidadDe.set("°F")
                resu = round((temp - 32)*5/9,3)
                resu = str(resu)+ "°C"
                self.resultado.set(resu)
            elif(op==4):
                self.unidadDe.set("°F")
                resu = round((temp - 32)*5/9+ 273.15,3)
                resu = str(resu)+ "°K"
                self.resultado.set(resu)
            elif(op==5):
                self.unidadDe.set("°K")
                resu = round(temp - 273.15,3)
                resu = str(resu)+ "°C"
                self.resultado.set(resu)
            elif(op==6):
                self.unidadDe.set("°K")
                resu = round((temp - 273.15)* 9/5 + 32,3) 
                resu = str(resu)+ "°F"
                self.resultado.set(resu)
        else:
            self.resultado.set("")
            self.unidadDe.set("")
Convertidor = Tk()
Convertidor.title("Convertidor de Temperatura")
Convertidor.geometry("600x200")

root = PyApp(Convertidor).grid()

Convertidor.mainloop()