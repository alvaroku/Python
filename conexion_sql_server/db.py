"""Conexión a una base de datos de SQL Server"""
#importar libreria
import pyodbc

#datos de conexion
direccion_servidor = 'LAPTOP-MO1HC59V'
nombre_bd = 'registro'
nombre_usuario = 'sa'
password = '2305'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
    print("-------------")
    print("Conectado")
    print("-------------")

except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)