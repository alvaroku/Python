from db import conexion

try:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT*FROM users;")

        user = cursor.fetchone()

        while user:
            print(user)
            user = cursor.fetchone()

except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()