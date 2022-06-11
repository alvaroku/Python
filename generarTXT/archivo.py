#importa la libreria string para poder acceder a susclases y metodos
import string
#importa la libreria os para poder realizar operaciones dependiente del Sistema Operativo como crear una carpeta y crear archivos
import os
#esta es una funcion que recibe como parametro una ruta de algun direcotrio 
def generar_archivos(ruta):
    #crea un directorio en base a la ruta dada como parametro
    os.makedirs(ruta)

#se crea la variable ruta 
ruta = 'NRC4535/letras'
#llama a la funcion para mandarle como parametro la ruta, y asi esta pueda crear el directorio 
generar_archivos(ruta)
#ciclo for que recorre las letras del abecedario
for i in string.ascii_uppercase:
    #abre un archivo txt almacenado en el directorio creado, que tiene como nombre cada letra del abecedario, en caso de que no exista el archivo, se crea 
    with open(os.path.join(ruta, '%s.txt' %i), 'w', encoding= 'utf-8') as f:
        # en el archivo actual del ciclo, escribe la letra del abecedario actual
        f.writelines(i)


#en general, este programa crea un directorio, en base a una ruta dada, de ahi hace un ciclo recorriendo todas
#las letras del abecedario para crear un archivo txt por cada una de ellas, en el cual se escribe la letra correspondiente en cada iteracion del ciclo
