#ABEL MOSALI MENDEZ LOPEZ

from tkinter import *
 
class PyApp(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()
        
 
    def createWidgets(self):
        self.codigo = StringVar()

        self.opcion = StringVar()
        self.opcion.set(0)

        self.resultado = StringVar()

        self.EtiquetaTitulo = Label(self,font=("Arial", 20),text="CAPACITOR CERAMICO")
        self.EtiquetaTitulo.grid(row=2, column=0)

        self.EtiquetaEntrada = Label(self,font=("Arial", 15),text="Código del capacitor")
        self.EtiquetaEntrada.grid(row=4, column=0)
        
        self.entrada = Entry(self, font=("Arial", 20),width=10, textvariable=self.codigo)
        self.entrada.insert(0, "0")
        self.entrada.grid(row=5, column=0)
#
        #self.EtiquetaUnidadDe = Label(self,font=("Arial", 20),textvariable=self.unidadDe)
        #self.EtiquetaUnidadDe.grid(row=2, column=15)
#
        self.ceButton = Button(self, font=("Arial", 12), text="Calcular", command=self.Calcular,width=10)
        self.ceButton.grid(row=2, column=20)
#
        self.EtiquetaResultado = Label(self,font=("Arial", 24),textvariable=self.resultado)
        self.EtiquetaResultado.grid(row=15, column=0)

        values = {
            "pF" : "1",
            "uf" : "2",
            "nF" : "3"
            }
        c = 1
        for (text, value) in values.items():
            r = Radiobutton(self.master, text = text, variable =self.opcion,value = value)
            r.grid(row=0, column=c)
            c+=1
    
    def Calcular(self):
        if(self.codigo.get()!=""):
            op = int(self.opcion.get())
            cod = self.codigo.get()
            resu = ""
            if len(cod)==2:
                resu = cod
            elif len(cod)==3:
            
                numero = cod[0:2]
                resu = str(numero)
                ceros = int(cod[-1])
                c= ""
                for i in range(ceros):
                    c+="0"
                resu +=c
            else:
                resu=0



            if(op==0):
                resu = int(resu)
                resu = resu*.000001
                resu = str(resu)+" uF"
                self.resultado.set(resu)
            elif(op==1):
                resu = str(resu)+" pF"
                self.resultado.set(resu)
            elif(op==2):
                resu = int(resu)
                resu = resu*.000001
                resu = str(resu)+" uF"
                self.resultado.set(resu)
            elif(op==3):
                resu = int(resu)
                resu = resu*.001
                resu = str(resu)+" nF"
                self.resultado.set(resu)
              
        else:
            self.resultado.set("")
App = Tk()
App.title("Capacitor App")
App.geometry("600x200")

root = PyApp(App).grid()

App.mainloop()