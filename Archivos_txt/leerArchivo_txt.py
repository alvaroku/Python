
file = open('datos.txt','r')

#print(file.read())
 
lista = []
for linea in file:
    print(linea)
    lista+=[linea.replace("\n",'')]
    
print(lista)
file.close()

