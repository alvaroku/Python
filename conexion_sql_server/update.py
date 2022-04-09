from db import conexion
try:
    with conexion.cursor() as cursor:

        consulta = "update users set first_name = ?, last_name = ? where id = ?;"
        nuevo_nombre = "dayana"
        nuevo_apellido = "xool"
        id_editar = 9
        cursor.execute(consulta, (nuevo_nombre,nuevo_apellido, id_editar))

    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
except Exception as e:
    print("Ocurrió un error al editar: ", e)
finally:
    conexion.close()