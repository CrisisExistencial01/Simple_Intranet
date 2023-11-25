import csv
import os
import getpass # Para ingresar contraseñas :D
# PATHS: Todas las rutas implementadas, es mas facil cambiarlas luego
path_Usuarios = 'Data/Users/Users.csv'
path_Profesores = 'Data/Users/Profesores.csv'
path_Estudiantes = 'Data/Users/Estudiantes.csv'
class Admin:
    def addUser(self):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: ")
        l = []
        if rol == "1":
            user = (rut, nombre, "Estudiante", l)
        elif rol == "2":
            user = (rut, nombre, "Profesor", l)
        else:
            print("Opción no válida, intente nuevamente")
        
        self.save(path_Usuarios, user)
        print("Usuario agregado exitosamente")
    def find(self, rut, lista):
        for i in lista:
            if i[0] == rut:
                return lista.index(i)
        return None
    def delUser(self, rut, Intranet): # users es la lista cargada en App.users
        rut = input("Ingrese el rut del usuario a eliminar: ")
        search = self.find(rut, Intranet.users)
        if search == None:
            print("Usuario no encontrado :/")
        else:
            confirm = input(f"Se ha encontrado al usuario {rut}, desea removerlo del sistema? s/n: ")
            if confirm.lower == "s":
                Intranet.user.remove[search]
    def save(self, path, data): 
        with open(path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)        
            
class Profesor:
    def __init__(self, rut, passwd, nombre, ramos):
        pass
    def modificarNota(self, estudiante, ramo, notas):
        # notas debe ser una tupla de la forma: (cualNota, valorNota)
        pass
    def verNotasmodulo():
    	with open(path_Profesores, 'r') as lectura:
    	 
    def verRamos():
    	with open(path_profesores,'r') as lectura:
    	  leer=csv.reader(lectura)
    	  
    def modNotasEstudiante():
    
    def verAlumnoMod():
    	with open(path_Profesores,'r') as lectura:
    	
    
    
    	
class Estudiante:
    def __init__(self, rut, nombre, ramos):
        self.ramos = ramos
    def inscribirRamo(self, ramo):
        self.ramos.append[ramo]
    # Ramo es el indice del ramo
    def botarRamo(self, index):
        self.ramos.remove[ramo]
class Ramo:
    # datos es una tupla con (Codigo, modulos asociados)
    def __init__(self, datos, cantidadNotas):
        self.datos = datos
        self.cantidadNotas = cantidadNotas

class App:
    def __init__(self):
        self.users = self.LoadUsers()
        self.estudiantes = self.LoadStudents()
        self.profesores = self.LoadTeachers()
        self.rut = None
        self.passwd = None # Nota: puede no ser necesario
    def LoadUsers(self):
        with open(path_Usuarios, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            users = list( tuple(row) for row in reader)
            return users
    def LoadStudents(self):
        estudiantes = []
        with open(path_Estudiantes, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar la primera fila de encabezados
            for row in reader:
                rut = row[0]
                nombre = row[1]
                ramos = row[2:]
                estudiante = Estudiante(rut, nombre, ramos)
                estudiantes.append(estudiante)
        return estudiantes
    def LoadTeachers(self):
        profesores = []
        with open(path_Profesores, newline='') as csvfile:
            reader = csv.reader(csvfile)
            #next(reader)
            for row in reader:
                rut = row[0]
                nombre = row[1]
                ramos = row[2:]
                profesor = Profesor(rut, nombre, ramos)
                profesores.append(profesor)
        return profesores
    def login(self):
        rut = input("Ingrese su rut: ")
        passwd = getpass.getpass("Ingrese su contraseña: ") # Asi la contraseña no se ve :D
        if rut == "ADMIN" and passwd == "NIMDA":
            self.user = Admin()
        else:
            for user in self.users:
                if user[0] == rut and user[1] == passwd:
                    self.rut = rut
                    self.passwd = passwd

            if self.user != None and user[2] == "Estudiante":
                self.user = self.makeEstudiante()
            if self.user == None: # Si no se encuentra el usuario
                self.clear()
                print("Usuario o contraseña incorrectos :(")
    def logout(self):
        self.rut = None
        self.passwd = None
    def makeEstudiante(self):
        self.user = Estudiante() # Se crea un objeto estudiante
    def makeProfesor(self):
        sel.user = Profesor()
    def clear(self): # Función para limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
    def adminMenu(self):
        print("(1) Agregar un Usuario")
    def run(self):
        while True:
            print("-------------Simple Intranet!--------------")
            opt = int(input("(1) Iniciar Sesion\n(2) Salir"))
            if opt == 1:
                self.login()
                if isinstance(self.user, Admin):
                    print("Bienvenido, Admin!!\n¿Que puedo hacer por ti?")
                elif isinstance(self.user, Estudiante):
                    print("Bienvenido, Estudiante!!")
            elif opt == 2:
                print("Saliendo...")
                break
    def menu_Profesor:
      while True:
    	menuPP=input("(1)\n modificar una nota\n (2) ver notas por modulo\n (3) ver ramos\n (4) modificar notas de estudiante\n (5) ver alumnos por modulo\n (6) salir")
    	if menuPP==1:
    	  modificarNota()
    	elif menuPP==2:
    	  verNotasModulo()
    	elif menuPP==3:
    	  verRamos()
    	elif menuPP==4:
    	  modNotasEstudiante()
    	elif menuPP==5:
    	  verAlumnoMod()
    	elif menu==6:
    	  break
    	else: 
    	  print("opción invalida")
    	  
   def menu_Estudiante:
   	while True:
   	  menuEE=input("(1) ver notas por modulo\n (2) ver ramos inscrito\n (3) inscribir ramos\n (4) botar ramos\n (5) salir")
   	  if menuEE==1:
   	    verNotasM()
   	  elif menuEE==2:
   	    verRamos()
   	  elif menuEE==3:
   	    incribirRamos()
   	  elif menuEE==4:
   	    botarRamos()
   	  elif menuEE==5:
   	    break
   	  else:
   	    print("opción invalida")

intranet = App()
intranet.run()
