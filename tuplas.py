t = ("Python", True, "Zope", 5)

print(t)
print(t[1])
print(t.index(True))


for i in t:
    print(i)
    
conexion_bd = "127.0.0.1","root","qwerty","nomina"
print ("Conexión típica:", conexion_bd)
print (type(conexion_bd))

conexion_completa = conexion_bd, "3307","10"
print(conexion_completa)

print ("IP de la BD:",  conexion_completa[0][0])

print(conexion_bd[0:2])
