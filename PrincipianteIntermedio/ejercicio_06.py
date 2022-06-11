prefijos = 'JKLMNOPQ'
sufijo = 'ack'

for letra in prefijos:
    if letra == 'Q' or letra == 'O':
        print(letra+'u'+sufijo)
    else:
        print(letra+sufijo)
    
