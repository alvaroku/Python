from db import conexion
import random
names = ['juan', 'pedro', 'laura', 'carmen', 'susana','monserrat']
last_names = ['perez', 'pech', 'canul', 'uitz', 'uribia','tun']
ages = [22,32,23,18,24]
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO users(first_name,last_name,edad) VALUES (?, ?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (random.choice(names),random.choice(last_names),random.choice(ages)))
        print("Insertado")
except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()