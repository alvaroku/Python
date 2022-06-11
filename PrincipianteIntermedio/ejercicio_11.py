import random

def poker(tupla):
    tuplaNumeros = ()
    for i in tupla:
        numero = i[:2]# de cada carta obtener la parte numerica
        tuplaNumeros+=numero,#agregarla a una tupla

    for i in tuplaNumeros:
        if tuplaNumeros.count(i)==4:
            return True
        else:
            return False
   
def generarBarajas(valores,forma):
    barajas = ()
    for i in valores:
        barajas+=f'{i} de {forma}',
    return barajas

def revolver(barajas):
    revuelto = ()
    for i in range(len(barajas)):
        carta = random.choice(barajaCompleta)
        while carta in revuelto:
            carta = random.choice(barajaCompleta)
        revuelto+=carta,
    return revuelto
            
valores = 'A',2,3,4,5,6,7,8,9,10,'J','Q','K'
formas = 'diamante','trebol','espada','corazon'

diamantes = generarBarajas(valores,formas[0])
treboles = generarBarajas(valores,formas[1])
espadas = generarBarajas(valores,formas[2])
corazones = generarBarajas(valores,formas[3])

barajaCompleta = diamantes[0:]+treboles[0:]+espadas[0:]+corazones[0:]

while True:
    jugada = ()
    barajasRevueltas = revolver(barajaCompleta)

    for i in range(5):
        carta = random.choice(barajasRevueltas)
        while carta in jugada:
            carta = random.choice(barajaCompleta)
        jugada+=carta,

    print('...................................')
    print(jugada)
    print('...................................')

    #p = poker(jugada)
    if poker(jugada):
        print('******************')
        print('Tiene un poker!!!')
        print('******************')
    else:
        print('xxxxxxxxxxxxxxxxxx')
        print('No tiene un poker')
        print('xxxxxxxxxxxxxxxxxx')

    #if p:
     #   break

     
    op = int(input('Jugar de nuevo?\n 1.Si\n 2.No\nIngrese una opción: '))
    if op !=1 :
        break
 



