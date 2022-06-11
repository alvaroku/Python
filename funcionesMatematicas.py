
import matplotlib.pyplot as plt
import numpy as np



def f(x):
    y = ( x**3 / 2) - x**3 - x + 1
    return y
    
def graficar(xL,yL):
    plt.plot(xL,yL,linewidth=1,color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.show()
    
def generarValX():
    x = np.arange(-10,11)
    y = f(x)
    graficar(x,y)
    print(x)
    



#generar valores de x
generarValX()



'''
xLista=[]
yLista=[]
#capturar valores de x
for i in range(10):
    x = float(input('Ingrese el valor de x:'))
    y = f(x)
    
    xLista+=[x]
    yLista+=[y]
   
graficar(xLista,yLista)
'''
