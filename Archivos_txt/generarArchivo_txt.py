

file=open("datos.txt","w")

for i in range(10):
    file.write("Línea "+str(i+1)+'\n') 

print('Guardado')
file.close()
