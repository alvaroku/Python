import random

def comparar(p1,cpu):
    if p1 == 'piedra':
        if cpu == 'papel':
            print('gana cpu')
        elif cpu == 'tijera':
            print('gana p1')
        else:
            print('empate')
    elif p1 == 'papel':
        if cpu == 'piedra':
            print('gana p1')
        elif cpu == 'tijera':
            print('gana cpu')
        else:
            print('empate')
    elif p1 == 'tijera':
        if cpu == 'piedra':
            print('gana cpu')
        elif cpu == 'papel':
            print('gana p1')
        else:
            print('empate')

opciones = ["piedra",'papel','tijera']

jugador1 = random.choice(opciones)
cpu = random.choice(opciones)
print('p1->',jugador1)
print('cpu->',cpu)

comparar(jugador1,cpu)