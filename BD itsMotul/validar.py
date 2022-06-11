
#codigo para validar los datos de entrada del usuario 

import re #libreria de expresiones regulares
from string import ascii_lowercase # alfabeto en minuscula

#valida entradas de texto
def Texto(n):
    n=n.lower()
    while True:
        correcto=True
        
        for i in n:
           if i not in alfabeto:
               correcto=False
               break

        if correcto==True and len(n)>0:
            break
        else:
            n=input('Ingrese solo texto:').lower()
            
    return n

#valida entradas de matricula
def Matricula(m):
     while True:
        if m.isdigit() and len(m)==8:
            break
        else:
            m=input('Ingrese un número de 8 dígitos:')
     return m  

#valida correos        
def Mail(c):
    c=c.lower()
    while True:
        if mailValido.search(c): # Comprobemos sí este es un correo electronico valido
              break
        else:
             c=input('Ingrese un correo válido:').lower()
    return c
    
#valida correos           
def MailPers(c):
    c=c.lower()
    while True:
        if mailValido.search(c) or c=='': # Comprobemos sí este es un correo electronico valido
              break
        else:
             c=input('Ingrese un correo válido:').lower()
    return c

#valida fechas de nacimiento
def FechaNac(f):
    while True:
        if fechaValida.search(f):
            break
        else:
             f=input('El formato debe ser:(dd/mm/aaaa):')
    return f

#valida numeros de telefono           
def Tel(t):
    while True:
        if t.isdigit() and len(t)==10 or t=='':
             break
        else:
            t = input('Ingrese un número válido:')
    return t

#valida que la entrada sea h o m       
def Sexo(s):
    s=s.lower()
    while True:
        if s=='h' or s=='m':
            break
        else:
            s=input('Ingrese una opción válida(h/m):').lower()
    return s

#valida opciones de si o no
def YesNo(o):
    o=o.lower()
    while True:
        if o == 's':
            break
        elif o == 'n':
            break
        else:
            o=input('Ingrese una opción válida(s/n):').lower()
    return o

#valida opciones numericas
def OpNumerica(n,lim):
    while True:
        if n.isdigit() and int(n)>0 and int(n)<=lim:
            n=int(n)
            break
        else:
            n=input('Ingrese una opción válida:')
    return int(n)

#################

#valida el formato de la clave para materias
def ClaveAsignatura(c):#ABC-123
    b=True
    while True:
        aux1=''
        aux2=''
        c=list(c)#convertir a lista
        for i in range(len(c)):
            if c[i]!='-':
                if c[i].isalpha():
                    aux1+=c[i]
                elif c[i].isdigit():
                    aux2+=c[i]
                    
        if len(aux1)==3 and len(aux2)==4 and c[3]=='-':
            c=aux1.upper()+'-'+aux2
            break
        else:
            c = input('La clave debe tener formato(ABC-1234):')
    return c

#valida el formato de los creditos de materias
def Creditos(cr):
    while True:
        form='0-0-0'
        aux=''
        for i in range(len(cr)):
            if len(cr)==5:
                if cr[i].isdigit():
                    aux+='0'
                elif cr[i]=='-':
                    aux+='-'
        if form==aux:
            break
        else:
             cr = input('El formato de los créditos debe ser(0-0-0):')       
    return cr
#################
    
#expresion regular para mails    
mailValido = re.compile(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}")
#expresion regular para fechas de nacimiento
fechaValida = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')
#alfabeto en minuscula
alfabeto= ascii_lowercase + 'ñáéíóú '

