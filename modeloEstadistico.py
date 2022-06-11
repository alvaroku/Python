#py -m pip install tk
from tkinter import messagebox  
import tkinter as tk
import math

'''messagebox.showinfo(message="Mensaje", title="Título")
messagebox.showwarning(message="Mensaje", title="Título")

print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
print(messagebox.askokcancel(message="¿Desea continuar?", title="Título"))
print(messagebox.askretrycancel(message="¿Desea reintentar?", title="Título"))

'''


def Calcular():
    try:  
        B = int(b.get()) #tasa por unidad de tiempo
        K = float(k.get()) #costo fijo
        h = float(H.get()) #costo por mantener una unidad en invenatio
        demora = int(dem.get()) #tiempo de demora
        
        y = math.sqrt( (2*K*B) / h )
        
        t = y/B

        longitud = t

        diferencia = demora - longitud

        u = diferencia * B

        messagebox.showinfo(message="Se debe hacer un pedido de {0} unidades cuando el stock llegue a {1} unidades ".format(y,u), title="Resultado")
        
    except:
        messagebox.showwarning(message="Por favor ingrese valores numéricos", title="Alerta")
        
w=450
h=250
ventana= tk.Tk() #crear ventana
ventana.title('Modelo Estadístico de un Artículo') #titulo ventana
ventana.config(width=w, height=h) # definir ancho y alto

#declarar variables que se obtendran en las cajas de texto
b = tk.StringVar()
k = tk.StringVar()
H = tk.StringVar()
dem = tk.StringVar()

#crear labels 
tk.Label(ventana, text="Tasa por unidad de tiempo").place(x=10,y=10)
tk.Label(ventana, text="Costo fijo").place(x=10,y=50)
tk.Label(ventana, text="Costo por mantener una unidad en inventario").place(x=10,y=90)
tk.Label(ventana, text="Demora").place(x=10,y=130)
tk.Label(ventana, text="Resultado", font=('Arial',20)).place(x=250,y=100)

#crear cajas de texto     e1 = tk.Entry(ventana,bg='red',fg='white',textvariable = b).place(x=10,y=30)
e1 = tk.Entry(ventana,bg='black',fg='white',textvariable = b).place(x=10,y=30)
e2 = tk.Entry(ventana,bg='black',fg='white',textvariable = k).place(x=10,y=70)
e3 = tk.Entry(ventana,bg='black',fg='white',textvariable = H).place(x=10,y=110)
e4 = tk.Entry(ventana,bg='black',fg='white',textvariable = dem).place(x=10,y=150)
#crear button
button = tk.Button(ventana, text="Calcular",command=Calcular).place(x=10,y=190)

#mostrar ventana
ventana.mainloop()
