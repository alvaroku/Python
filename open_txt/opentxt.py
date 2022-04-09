
file = open("demo.txt", "a")
file.write("hola\n")
file.close()

file = open("demo.txt", "r")
#print(file.readlines())
for i in file.readlines():
    print(i,end="")
file.close()