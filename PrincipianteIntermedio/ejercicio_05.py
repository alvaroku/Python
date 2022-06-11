def salto():
    print('---------------------------------------------')
    
def capturarNotas():
    for i in range(len(materias)):
        auxNotas = []
        suma = 0
        for j in range(3):
            nota = float(input(f'Ingrese la nota {j+1} de la materia {materias[i]}: '))
            suma+=nota
            auxNotas+=[nota]
        promedios.append(suma/3)
        notas.append(auxNotas)
        salto()
            
def mostrarDatos(listaProm,tamanio):
    for i in range(tamanio):
        print(materias[i],'\t', end="")
        for n in notas[i]:
            print(n,'\t',end="")

        print(promedios[i],'\t',end="")
        print()
   
def obtenerPromedioGeneral():
    suma = 0
    for i in promedios:
        suma+=i
        
    return suma/len(promedios)

def obtenerMayor():
    mayor = 0
    for i in promedios:
        if i>mayor:
            mayor = i
    return mayor

def capitalizar(cadena):
    return cadena[0].upper()+cadena[1:]

 
  
res = 1

materias = ['Matemáticas Discretas', 'Programación','Inglés','Cálculo Integral',
            'Álgebra Lineal']
promedios = []
notas = []
while res==1:
    nombre = capitalizar(input('Nombre del alumno: ').lower())
    apellido = capitalizar(input('Apellido del alumno: ').lower())
    salto()
    
    capturarNotas()

    print(nombre, apellido)
    mostrarDatos(promedios,len(promedios))
    
    print('\t'*3,'Promedio general: ', obtenerPromedioGeneral())
    mayor = obtenerMayor()
    print(f'La materia con mejor promedio es {materias[promedios.index(mayor)]} con un promedio de {mayor}')
    salto()
    
    print('Desea ingresar otro alumno?')
    print(' 1.Sí\n 2.No')
    res = int(input('Ingres el número de opción: '))
    salto()
    promedios = []
    notas = []

print(f'Adios {nombre} {apellido}, vuelve pronto')
