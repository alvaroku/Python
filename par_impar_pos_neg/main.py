lista = [1,5,3,55,34,-5,-123,2,10,24,0]
contPar = 0
contImpar = 0
contPos = 0
contNeg = 0

for i in lista:
    if i%2==0:
        contPar+=1
    else:
        contImpar+=1

    if i < 0:
        contNeg+=1
    else:
        contPos+=1
print('Pares:',contPar)
print('Impares:',contImpar)
print('Positivos:',contPos)
print('Negativos:',contNeg)