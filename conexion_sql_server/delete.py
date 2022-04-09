from db import conexion
try:
    with conexion.cursor() as cursor:

        consulta = "DELETE FROM users WHERE id=?;"
        id = 7
        cursor.execute(consulta, (id))

    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
except Exception as e:
    print("Error eliminando: ", e)
finally:
    conexion.close()