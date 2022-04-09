from random import random
from db import conexion
import random
ids = [1,2,3,4,5,6,7]
try:
    with conexion.cursor() as cursor:

        consulta = "SELECT*FROM users WHERE id = ?;"
        cursor.execute(consulta, (random.choice(ids)))

        user = cursor.fetchone()

        while user:
            print(user)
            user = cursor.fetchone()
            
except Exception as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexion.close()