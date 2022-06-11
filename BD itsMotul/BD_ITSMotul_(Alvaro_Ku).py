#Alvaro Daniel Kú Uitz
    #2°A ISC
import MySQLdb
from string import ascii_lowercase
from string import ascii_uppercase
import random
import os
import validar
import datetime, locale
import time
class DB:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = '2305'
    DB_NAME = 'anecdotario'
     
    def run_query(self,query=''):
        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]
         
        conn = MySQLdb.connect(*datos) # Conectar a la base de datos
        cursor = conn.cursor() # Crear un cursor
        cursor.execute(query) # Ejecutar una consulta
         
        if query.upper().startswith('SELECT'):
            data = cursor.fetchall() # Traer los resultados de un select
        else:
            data = conn.affected_rows()
            conn.commit() # Hacer efectiva la escritura de datos

        cursor.close() # Cerrar el cursor
        conn.close() # Cerrar la conexión
         
        return data

      
class Maestro(DB):       
#-Metodo para Login-
    #selecciona el registro de un maestro donde su correo y contraseña sean iguales a los ingresados
    def queryLogin(self,u,p):
        query = "SELECT*from maestro WHERE correo = '{0}' and contra = '{1}'".format(u,p)
        result=self.run_query(query)
        return result  
    
#-Clase Alumno-
class Alumno(DB):
    #constructor de la clase alumno
    def __init__(self,n='',a='',m='',car='',ci='',cp='',f='',p='',t='',s=''):
        self.nom = n
        self.ape = a
        self.mat = m
        self.carr = car
        self.corIns = ci
        self.corPer = cp
        self.fechaN = f
        self.proc = p
        self.tel = t
        self.sexo = s  
    #métodos que regresan atributos de la clase alumno    
    def dameNom(self):
        return self.nom 
    def dameApe(self):
        return self.ape 
    def dameMat(self):
        return self.mat 
    def dameCar(self):
        return self.carr 
    def dameCorIns(self):
        return self.corIns 
    def dameCorPer(self):
        return self.corPer 
    def dameFechaN(self):
        return self.fechaN 
    def dameProc(self):
        return self.proc 
    def dameTel(self):
        return self.tel
    def dameSex(self):
        return self.sexo
#-metodos para la tabla alumnos-

    #selecciona todo los registros de la tabla alumnos
    def querySelectTodoAl(self):
        query = "SELECT * FROM alumno"
        result = self.run_query(query)
        return result
    
    #inserta los atributos del objeto almuno en la tabla alumnos de la BD
    def queryInsertarAl(self,al):
        n = al.dameNom()
        a = al.dameApe()
        m = al.dameMat()
        c = al.dameCar()
        cIns = al.dameCorIns()
        cPer = al.dameCorPer()
        fN = al.dameFechaN()
        proc = al.dameProc()
        tel = al.dameTel()
        s = al.dameSex()
        query = "INSERT INTO alumno (matricula,nombres,apellidos,carrera,cins,cper,fnac,proc,tel,genero) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(m,n,a,c,cIns,cPer,fN,proc,tel,s)
        result=self.run_query(query)

    #actualiza el dato pass(contraseña)de la BD de la matricula seleccionada
    def queryPassAl(self,m,p):
        query = "UPDATE alumno SET pass='{0}' WHERE matricula = '{1}'".format(p,m)
        result=self.run_query(query)

    #elimina un registro de la BD 
    def queryEliminarAl(self,c):
        #Eliminar registros
        mat=c
        query = "DELETE FROM alumno WHERE matricula = '{0}'".format(mat)
        result=self.run_query(query)

    #actualiza el dato telefono de la BD de la matrcula seleccionada  
    def queryActTel(self,m,t):
        mat=m
        tel=t
        query = "UPDATE alumno SET tel='{0}' WHERE matricula = '{1}'".format(tel,mat)
        result=self.run_query(query)

    #actualiza el dato del correo personal en la BD de la matricula selecionada  
    def queryActCorPer(self,m,c):
        mat=m
        cor=c
        query = "UPDATE alumno SET cper='{0}' WHERE matricula = '{1}'".format(cor,mat)
        result=self.run_query(query)
        
    #busca un alumno usando la matricula  
    def buscarAl(self,m):
        mat=m
        query = "SELECT*from alumno WHERE matricula = '{0}'".format(mat)
        result=self.run_query(query)
        return result
    

#-Clase Asignatura-
class Asignatura(DB):
    #constructor de la clase asignatura
    def __init__(self,cl='',nom='',cre='',sem=''):
        self.clave=cl
        self.nom=nom
        self.cre=cre
        self.sem=sem
    #metodos que regresan atributos de la clase asignatura
    def dameClave(self):
        return self.clave
    def dameNom(self):
        return self.nom
    def dameCre(self):
        return self.cre
    def dameSem(self):
        return self.sem

    #-Metodos para la tabla asignatura-

    #selecciona todo los registros de la tabla asignatura
    def querySelectTodoAsign(self):
        query = "SELECT * FROM asignatura"
        result = self.run_query(query)
        return result

    #inserta los atributos del objeto asignatura en la tabla asignaturas de la BD
    def queryInsertarAsign(self,a):
        c = a.dameClave()
        n = a.dameNom()
        cr = a.dameCre()
        s = a.dameSem()
        
        query = "INSERT INTO asignatura (clave,nombre,creditos,semestre) VALUES ('{0}','{1}','{2}','{3}')".format(c,n,cr,s)
        result=self.run_query(query)
        

#-Clase Asistencia    
class Asistencia(DB):
    #constructor de la clase asistencia
    def __init__(self,a='',m='',d='',h='',s=''):
        self.asign = a
        self.matr = m
        self.dia = d
        self.hora = h
        self.status = s
    #metodos que retornan atributos de la clase asistencia
    def dameAsign(self):
        return self.asign   
    def dameMatr(self):
        return self.matr
    def dameDia(self):
        return self.dia 
    def dameHora(self):
        return self.hora 
    def dameStat(self):
        return self.status

    #-Metodos para la tabla asistencia-

    #selecciona todos los registros de la tabla asistencia
    def querySelectTodoAsis(self):
        #Seleccionar todos los registros
        query = "SELECT * FROM asistencias"
        result = self.run_query(query)
        return result

    #busca las asistencias de la matricula recibida
    def buscarAsis(self,m):
        query = "SELECT * FROM asistencias WHERE matricula = '{0}'".format(m)
        result=self.run_query(query)
        if len(result)>0:
            print('*Asistencias*')
            for i in result:
                print(i)
        else:
            print('No hay resultados')

    #inserta los atributos del objeto asistencia en la tabla asistencia de la BD
    def queryInsertarAsis(self,a):
        asign = a.dameAsign()
        mat = a.dameMatr()
        d = a.dameDia()
        h = a.dameHora()
        s = a.dameStat()          
        query = "INSERT INTO asistencias (asignatura,matricula,dia,hora,status) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(asign,mat,d,h,s)
        result=self.run_query(query)

    #selecciona todas las matriculas de la tabla alumnos  
    def querySelectMatr(self):
        query = "SELECT matricula FROM alumno"
        result=self.run_query(query)
        return result
    
    #selecciona el nombre del alumno usando la matricula
    def querySelectNombreAl(self,m):
        query = "SELECT nombres FROM alumno WHERE matricula = '{0}'".format(m)
        result=self.run_query(query)
        return result

    #selecciona las materias usando el semestre
    def querySelectAsign(self,sem):
        query = "SELECT * FROM asignatura WHERE semestre = '{0}'".format(sem)
        result=self.run_query(query)
        return result

    #selecciona el nombre de la materia en base a su clave
    def querySelectNomAsign(self,cl):
        query = "SELECT nombre FROM asignatura WHERE clave = '{0}'".format(cl)
        result=self.run_query(query)
        return result
    

#-FUNCIONES-

    #funcion que obtiene y retorna el dia actual en español
def obtenerDia():
    locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')
    return time.strftime("%A")

    #funcion que obtiene y retorna la hora actual
def obtenerHora():
    return time.strftime("%H:%M:%S")

    #funcion que imprime los elementos de la lista de status
def mostrarStatus():
    print('Seleccionar status para el alumno')
    for i in range(len(status)):
        print('  '+str(i+1)+')'+status[i])
    print('--------------------')

    #funcion que genera una contraseña aleatoria
def generarPass():
    alfa= ascii_lowercase+'1234567890-_@'+ascii_uppercase 
    contra=''
    for i in range(15):
        contra+=alfa[random.randint(0,len(alfa)-1)]
    return contra
    

# -subMenuActualizar-
    #muestra un menu de opciones de actualizacion de datos
def subMenuAct():
    while True:
        print('''======================================
+ Opciones de actualización de datos +
======================================
 1)Correo personal
 2)Teléfono
 3)Volver
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        a = validar.OpNumerica(input('Ingrese una opción:'),3)
        os.system('cls')
        if a == 1:
            mat = validar.Matricula(input('Ingrese la matrícula:'))
            nuevo=validar.MailPers(input('Ingrese el nuevo correo:'))
            op = validar.YesNo(input('¿Desea continuar esta operación?(s/n):'))
            if op=='s':
                db.queryActCorPer(mat,nuevo)
        elif a == 2:
            mat = validar.Matricula(input('Ingrese la matrícula:'))
            nuevo=validar.Tel(input('Ingrese el nuevo número teléfono:'))
            op = validar.YesNo(input('¿Desea continuar esta operación?(s/n):'))
            if op=='s':
                db.queryActTel(mat,nuevo)
        else:
            break
    #funcion que muestra las carreras        
def carreras():
    ing=['Ingeniería en Sistemas Computacionales','Ingeniería Electromecánica',
         'Ingeniería Electrónica','Ingeniería Industrial','Ingeniería en Energías Renovables'] 
    print('''========================================
Carreras
========================================
Elija una de las carreras
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
    for i in range(len(ing)):
        print(str(i+1)+')'+ing[i])
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    
#-MENU ALUMNO-
    #muestra las acciones que puede realizar con los datos de un alumno
def menuAlumno():
    while True:
        print('''=============================
+    Opciones de alumnos    +
=============================
 1)Registrar alumno
 2)Eliminar alumno
 3)Actualizar datos
 4)Buscar
 5)Ver alumnos registrados
 6)Generar password
 7)Salir
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        o = validar.OpNumerica(input('Ingrese una opción:'),7)
        os.system('cls')
        if o == 1:
            while True:
                al = Alumno()
                m = validar.Matricula(input('Ingresar matrícula:'))
                r = al.buscarAl(m)
                if len(r)==1:
                    print('*Esta matrícula ya esta registrada*')
                else:
                    break
            
            n = validar.Texto(input('Ingresar nombre(s):'))
            a = validar.Texto(input('Ingresar apellido(s):'))
            carreras()
            op = validar.OpNumerica(input('Seleccione una opción:'),5)
            carr = inge[op-1]
            ci = validar.Mail(input('Ingresar correo institucional:'))
            cp = validar.MailPers(input('Ingresar correo personal(opcional):'))
            f = validar.FechaNac(input('Fecha de nacimiento:(dd/mm/aaaa):'))
            pr = validar.Texto(input('Lugar de procedencia:'))
            t = validar.Tel(input('Número de teléfono(opcional):'))
            s = validar.Sexo(input('Ingrese su sexo(h/m):'))
            al=Alumno(n,a,m,carr,ci,cp,f,pr,t,s)
            al.queryInsertarAl(al)#mandar el objeto alumno al metodo de DB para insertar
            print('Se registró un alumno!')
            print('======================')
            
        elif o == 2:
            al = Alumno()
            mat = validar.Matricula(input('Ingrese la matrícula:'))
            res=al.buscarAl(mat)
            print(res[0])
            op = validar.YesNo(input('¿Desea continuar esta operación?(s/n):'))
            if op=='s':
                al.queryEliminarAl(mat)
                
        elif o== 3:
            subMenuAct()
               
        elif o == 4:
            al = Alumno()
            mat = validar.Matricula(input('Ingrese la matrícula:'))
            res=al.buscarAl(mat)
            print(res[0])
            
        elif o == 5:
            al = Alumno()
            res = al.querySelectTodoAl()
            for i in res:
                print(i)
                
        elif o == 6:
            mat = validar.Matricula(input('Ingrese la matrícula:'))
            pw = generarPass()
            print('La contraseña para ',mat,' es ',pw)
            op = validar.YesNo(input('¿Desea continuar esta operación?(s/n):'))
            if op=='s':
                al= Alumno()
                al.queryPassAl(mat,pw)
                
        else:
            print('Gracias por usar nuestro sistema de registro')
            break

#-MENU ASIGNATURA-
    #muestra las acciones que puede realizar con los datos de una asignatura
def menuAsignatura():
    while True:
        print('''===========================
+ Registro de asignaturas +
===========================
1)Registrar asignaturas
2)Ver asignaturas
3)Salir
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        o = validar.OpNumerica(input('Ingrese una opción:'),3)
        os.system('cls')
        if o == 1:
            s = validar.OpNumerica(input('Semestre:'),9)
            c = validar.ClaveAsignatura(input('Ingrese la clave de la asignatura:'))
            n = validar.Texto(input('Ingrese el nombre de la asignatura:'))
            cr = validar.Creditos(input('Ingrese los créditos de la asignatura:'))
            a = Asignatura(c,n,cr,s)
            a.queryInsertarAsign(a)
        elif o == 2:
            a = Asignatura()
            res = a.querySelectTodoAsign()
            for d in res:
                print('Clave: '+d[0]+' | Nombre: '+d[1]+' | Créditos: '+d[2]+' | Semestre: '+str(d[3]))
        
        elif o == 3:
            break
        
#-MENU ASISTENCIA
     #muestra las acciones para realizar un pase de lista 
def menuAsistencia():
    while True:
        print('''==========================
+ Opciones de asistencia +
==========================
 1)Pase de lista
 2)Ver asistencias
 3)Buscar
 4)Salir
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        o = validar.OpNumerica(input('Ingrese una opción:'),4)
        os.system('cls')
        if o == 1:
            A = Asistencia()
            sem = validar.OpNumerica(input('Semestre:'),2)
            asign = A.querySelectAsign(sem) #hacer consulta para obtener claves de la tabla asign
            print('------------\nMaterias\n------------')
            for i in range(len(asign)):
                print(str(i+1)+')'+asign[i][1])
            print('------------')
            x = validar.OpNumerica(input('Ingrese una opción:'),len(asign))#num de materia
            
            matr= A.querySelectMatr()#obtener matriculas
            for i in range(len(matr)):#recorrer lista de matriculas
                a = asign[x-1][0]
                al= A.querySelectNombreAl(matr[i][0])#consultar nombre del alumno con matr
                print('Alumno '+str(i+1)+': '+al[0][0])
                m = matr[i][0]
                d = obtenerDia()
                h = obtenerHora()
                mostrarStatus()
                s = validar.OpNumerica(input('Ingrese una opción:'),len(status))
                A = Asistencia(a,m,d,h,s)
                A.queryInsertarAsis(A)
                
        elif o == 2:
            print('''=====================
ASISTENCIAS
=====================''')
            A = Asistencia()
            asis = A.querySelectTodoAsis()
            #print(asis)
            for i in range(len(asis)):
                clave = asis[i][1]
                a = A.querySelectNomAsign(clave)
             #   print(a)
                print('Asgnatura:',a[0][0],' | Matrícula:',asis[i][2],' | Día:',asis[i][3],
                      ' | Hora:',asis[i][4],' | Status:',status[asis[i][5]-1])
        elif o == 3:
            A = Asistencia()
            m = validar.Matricula(input('Ingrese la matrícula a buscar:'))
            A.buscarAsis(m)
        elif o == 4:
            break

def nombres():
    print('''******************************
   -ALVARO DANIEL KÚ UITZ
      -ALEX XUL CANCHE
******************************
           2°A ISC
******************************\n''')

    
#-MAIN MENU-
    #muestra el menu principal con sus opciones para cada uno de los apartados que se tienen
def mainMenu():
    while True:
        print('''==================
* MENÚ PRINCIPAL *
==================
 1)Ir al apartado de alumnos
 2)Ir al apartado de asistencias
 3)Ir al apartado de asignaturas
 4)Salir
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
        o = validar.OpNumerica(input('Ingrese una opción:'),4)
        os.system('cls')
        if o == 1:
            menuAlumno()

        elif o == 2:
            menuAsistencia()
            
        elif o == 3:
            menuAsignatura()

        else:
            break

def welcome():
    print('''===========================
        DESIGNED BY
===========================
   ALVARO DANIEL KÚ UITZ
===========================''')
    time.sleep(1)
    os.system('cls')
    
     
inge=['isc','iem','ie','ii','ier']#lista de carreras
status = ['falta','asistencia','llegó tarde','se fué temprano']#lista de status para alumnos

#crear objeto BD
#db=DB()
#nombres()

#-LOGIN-
    #se muestra un login para que el maestro pueda tener acceso a todas las opciones

welcome()

while True:
    print('''=============================
       LOGIN ITS MOTUL
=============================''')
    us = validar.Mail(input('Usuario:'))
    print('-----------------------------')
    pw = input('Contraseña:')
    print('-----------------------------')
    m = Maestro()
    r=m.queryLogin(us,pw)
    if len(r)==1:
        os.system('cls')
        mainMenu()
    else:
        print('*Usuario o contraseña incorrectos*')
 



