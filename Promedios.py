suma = 0
sumatotal=0

m = int(input('Cuantos materias?: '))
for i in range(m):
    print('Materia',i+1)
    suma=0
    nc = int(input('Cuantos parciales?: '))
    for j in range(nc):
        suma+=int(input('Ingrese una calificación'))
    prom = suma/nc
    print("Promedio: ",prom)
    sumatotal+=prom
    print('------------------------------')
print('Promedio final: ',sumatotal/m)
input()
    
