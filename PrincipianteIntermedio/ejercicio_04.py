def salto():
    print('---------------------------------------------')
    
def capturarNotas():
    for i in range(len(materias)):
        suma = 0
        for j in range(3):
            nota = float(input(f'Ingrese la nota {j+1} de la materia {materias[i]}: '))
            suma+=nota
        promedios.append(suma/3)
        salto()
            
def mostrarPromedios(listaProm,tamanio):
    for i in range(tamanio):
        print(f'El promedio de {materias[i]} es {listaProm[i]}')


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

res = 1

materias = ['Matemáticas Discretas', 'Programación','Inglés','Cálculo Integral',
            'Álgebra Lineal']
promedios = []

while res==1:
    nombre = input('Nombre del alumno: ')
    apellido = input('Apellido: ')
    salto()
    
    capturarNotas()
    mostrarPromedios(promedios,len(promedios))
    salto()
    
    print('Promedio general: ', obtenerPromedioGeneral())
    salto()

    mayor = obtenerMayor()
    print(f'La materia con mejor promedio es {materias[promedios.index(mayor)]} con un promedio de {mayor}')
    salto()
    
    print('Desea ingresar otro alumno?')
    print(' 1.Sí\n 2.No')
    res = int(input('Ingres el número de opción: '))
    salto()
    promedios = []

print(f'Adios {nombre} {apellido}, vuelve pronto')
