diccionario = {'nombre' : 'Carlos', 'edad' : 22,
               'cursos': ['Python','Django','JavaScript']}

print(diccionario['nombre'])#Carlos
print(diccionario['edad'])#22
print(diccionario['cursos'])#['Python','Django','JavaScript']


print(diccionario['cursos'][0])#Python
print(diccionario['cursos'][1])#Django
print(diccionario['cursos'][2])#JavaScript
#.copy()  para copiar
for key in diccionario:
  print(key, ":", diccionario[key])


dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
print(dic)

dic = dict(zip('abcd',[1,2,3,4]))
print(dic)

dic =   {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
ite = dic.items()#.values()   .keys()
print(ite)

 
keys= dic.keys()
print(keys)

values= dic.values()
print(values)

dic1 = dic.copy()
print(dic1)

dic = dict.fromkeys(['a','b','c','d'],1)
print(dic)

valor = dic.get('a')
print(valor)

valor = dic.pop('a')
print(valor)
print(dic)

dic.setdefault('e',5)
print(dic)

dic2 = {'a':9, 'b':45}
dic.update(dic2)
print(dic)

print()

cadena = 'alvarodaniel'
d = {}
for i in cadena:
  d[i] = d.get(i,0)+1

print(d)
print(sorted(d.items()))
print(len(d))
print(d.get('a',None))
