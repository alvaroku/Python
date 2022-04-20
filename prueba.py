e = int(input("edad: "))

if e <= 0:
    print("nadie tiene esa edad")
elif e >0 and e < 18:
    print("eres menor de edad")
elif e <= 100:
    print("eres mayor de edad")
else:
    print("edad no valida")

