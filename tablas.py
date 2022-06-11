def multiplos(n,tope):
    i=1
    while i<=tope:
        print(i*n,'\t',end='')
        i+=1
    print()

def tabla(tope):
    i=1
    while i<=tope:
        multiplos(i,tope)
        i+=1
    print()

tabla(10)


