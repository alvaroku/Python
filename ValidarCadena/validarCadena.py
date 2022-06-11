import tkinter as tk
from tkinter import messagebox as MessageBox

     
def gui():
    mensaje=""
    def validar():
        seleccion = False
        concatenacion = False
        d = False

        A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m', 'n',
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        C = [1,2,3,4,5,6,7,8,9,0]
        D = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡']


        identificador = '(A|B)CCCD'
        
        string = cadena.get()
        mensaje = ""
        if len(string) == 5:
           
            #seleccion
            if string[0]in A or string[0] in B:
                seleccion = True
            else:
                mensaje+='*Debe tener un caracter del alfabeto A ó B en la posición 1*\n'
            #conc
            try:
                int(string[1])in C and int(string[2])in C and int(string[3])
                concatenacion = True
            except:
                mensaje+='*Debe tener un caracter del alfabeto C en la posición 1,2 y 3*\n'

            if string[4] in D:
                d = True
            else:
                mensaje+='*Debe tener al final un caracter del alfabeto D*\n'

                
            #print(seleccion,concatenacion,d)
            if (seleccion == True and concatenacion== True and d==True):
                
                imagen=tk.PhotoImage(file="correcto.png").subsample(10)
                labelImg.config(image=imagen)
                
                MessageBox.showinfo(message="La cadena es correcta", title="Correcto")

            else:
                imagen=tk.PhotoImage(file="incorrecto.png").subsample(10)
                labelImg.config(image=imagen)
                
                MessageBox.showerror("Error",mensaje)
                

        else:
            imagen=tk.PhotoImage(file="incorrecto.png").subsample(5)
            labelImg.config(image=imagen)
            
            MessageBox.showwarning("Alerta", "La cadena debe tener 5 caracteres")
            
        
        #root.destroy()
    
    def reset():
        textBox.delete(0,"end")
  
   
    
    root = tk.Tk()
    root.geometry('400x200')
    root.title("Actividad 3: Validar Cadena")
    cadena = tk.StringVar()
    
    
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=1, pady=1)

    #carga de elementos
    label = tk.Label(frame, text="Igrese una cadena")
    label.grid(row=0, column=0, padx=5, pady=5)

    textBox = tk.Entry(frame, width=30, textvariable=cadena)
    textBox.grid(row=2, column=0, padx=5, pady=5)

    boton = tk.Button(frame, text="Validar", command=validar)
    boton.grid(row=2, column=1, padx=5, pady=5)
    
    boton2 = tk.Button(frame, text="Reiniciar", command=reset)
    boton2.grid(row=2, column=2, padx=5, pady=5)

    #carga label sin imagen
    labelImg=tk.Label(frame)
    labelImg.grid(row=4, column=0, padx=5, pady=5)

 
    root.mainloop()

 
if __name__ == "__main__":
    
    gui()
