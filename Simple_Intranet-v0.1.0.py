import csv
import os
import getpass # Para ingresar contraseñas :D
# PATHS: Todas las rutas implementadas, es mas facil cambiarlas luego
path_Usuarios = 'Data/Users/Users.csv'
path_Profesores = 'Data/Users/Profesores.csv'
path_Estudiantes = 'Data/Users/Estudiantes.csv'
# Colores AESTHETIC u.u
class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Admin:
    def addRamo(self):
        codigo = input("Ingrese el codigo del ramo: ")
        nombre = input("Ingrese el nombre del ramo: ")
        modulos = input("Ingrese los modulos del ramo: ")
        data = (codigo, nombre, modulos)
        self.save(path_Ramos, data)
        print("Ramo agregado exitosamente")
    def delRamo(self, Intranet):
        codigo = input("Ingrese el codigo del ramo a eliminar: ")
        search = self.find(codigo, Intranet.ramos)
        if search == None:
            print("Ramo no encontrado :/")
        else:
            confirm = input(f"Se ha encontrado al ramo {codigo}: {Intranet.ramos[search][1]}\n[{color.WARNING}*{color.RESET}] Desea eliminarlo? s/n: ")
            if confirm.lower == "s":
                Intranet.ramos.pop(search)
                self.saveList(path_Ramos, Intranet.ramos)
                print(f"[{color.OKGREEN}*{color.RESET}] Ramo eliminado exitosamente")
            else:
                print(f"[{color.FAIL}*{color.RESET}]Operación cancelada")

    def addUser(self):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: ")
        l = []
        if rol == "1":
            user = (rut, rut, nombre, "Estudiante")
            data = (rut, nombre, l[0:])
            self.save(path_Estudiantes, data)
        elif rol == "2":
            user = (rut, rut, nombre, "Profesor")
            data = (rut, nombre, l[0:])
            self.save(path_Profesores, data)
        else:
            print("Opción no válida, intente nuevamente")
        
        self.save(path_Usuarios, user)
        print("Usuario agregado exitosamente")
    def find(self, rut, lista):
        for i in lista:
            if i[0] == rut:
                return lista.index(i)
        return None
    def delUser(self, Intranet): # users es la lista cargada en App.users
        rut = input("Ingrese el rut del usuario a eliminar: ")
        search = self.find(rut, Intranet.users)
        if search == None:
            print(f"[{color.FAIL}*{color.RESET}] Usuario no encontrado :/")
        else:
            confirm = input(f"[{color.OKGREEN}*{color.RESET}] Se ha encontrado al usuario {color.BOLD}{rut}{color.RESET}\nDesea removerlo del sistema? s/n: ")

            if confirm.lower() == 's':
                print("DEBUG: Eliminación de usuario")
                # Eliminar el usuario de los archivos Estudiantes.csv o Profesores.csv
                if Intranet.users[search][3] == "Estudiante":
                    print("DEGUG: Eliminando estudiante")
                    Intranet.estudiantes.pop(search)

                    self.saveList(path_Estudiantes, Intranet.estudiantes)

                elif Intranet.users[search][3] == "Profesor":
                    print("DEGUG: Eliminando profesor")
                    profesor_indice = search
                    Intranet.profesores.pop(profesor_indice)
                    self.saveList(path_Profesores, Intranet.profesores)
                else:
                    print(f"[{color.FAIL}*{color.RESET}] Error al eliminar el usuario de los archivos de usuarios")
                # Eliminar el usuario de Users.csv
                Intranet.users.pop(search)
                self.saveList(path_Usuarios, Intranet.users)

                print(f"[{color.OKGREEN}*{color.RESET}] Usuario eliminado exitosamente")
            else:
                print(f"[{color.FAIL}*{color.RESET}] Operación cancelada")
    def save(self, path, data): # Guarda un dato en un archivo csv (data debe ser una tupla)
        with open(path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def saveList(self, path, data): 
        # Guarda una lista en un archivo csv 
        #(data debe ser una lista de tuplas)
        with open(path, "w", newline='') as f:
            writer = csv.writer(f)
            for i in data:
                writer.writerow(i)
    def modifyUser(self, Intranet):
        rut = input("Ingrese el rut del usuario a modificar: ")
        search = self.find(rut, Intranet.users)
        if search == None:
            print("Usuario no encontrado :/")
        else:
            confirm = input(f"Se ha encontrado al usuario {color.BOLD}{rut}{color.RESET}, desea modificarlo? s/n: ")
            if confirm.lower == "s":
                opt = input("¿Que desea modificar?\n(1) Rut\n(2) Nombre\n(3) Rol")
                if opt == "1":
                    Intranet.users[search][0] = input("Ingrese el nuevo rut: ")
                    if isinstance(Intranet.user, Estudiante):
                        Intranet.estudiantes[search][0] = Intranet.users[search][0]
                    elif isinstance(Intranet.user, Profesor):
                        Intranet.profesores[search][0] = Intranet.users[search][0]

                elif opt == "2":
                    Intranet.users[search][1] = input("Ingrese el nuevo nombre: ")
                    if isinstance(Intranet.user, Estudiante):
                        Intranet.estudiantes[search][1] = Intranet.users[search][1]
                    elif isinstance(Intranet.user, Profesor):
                        Intranet.profesores[search][1] = Intranet.users[search][1]
                elif opt == "3":
                    Intranet.users[search][3] = input("Ingrese el nuevo rol: ")
                    if isinstance(Intranet.user, Estudiante):
                        Intranet.estudiantes[search][3] = Intranet.users[search][3]

                    elif isinstance(Intranet.user, Profesor):
                        Intranet.profesores[search][3] = Intranet.users[search][3]
                Intranet.saveList(path_Usuarios, Intranet.users)
                print(f"[{color.OKGREEN}*{color.RESET}] Usuario modificado exitosamente")
            else:
                print(f"[{color.FAIL}*{color.RESET}] Operación cancelada")

    def menu(self, Intranet):
        while True:
            opt = int(input("(1) Agregar un Usuario\n(2) Eliminar un Usuario\n(3) Modificar un Usuario\n(4) Ver Usuarios\n(0) Salir\n:"))
            if opt == 1:
                self.addUser()
            elif opt == 2:
                self.delUser(Intranet)
            elif opt == 3:
                self.modifyUser(Intranet)
            elif opt == 4:
                for i in Intranet.users:
                    print(f"RUT: {color.BOLD}{i[0]}{color.RESET}\nNOMBRE: {i[2]}\nROL: {i[3]}\n")
            elif opt == 0:
                intranet.logout()
                break
            else:
                print(f"[{color.FAIL}*{color.RESET}] Opcion no valida, intente nuevamente")

            
        
class Profesor:
    def __init__(self, rut, nombre, ramos):
        pass
    def modificarNota(self, estudiante, ramo, notas):
        # notas debe ser una tupla de la forma: (cualNota, valorNota)
        pass

class Estudiante:
    def __init__(self, rut, nombre, ramos):
        self.rut = rut
        self.nombre = nombre
        self.ramos = ramos
    def inscribirRamo(self, ramo):
        self.ramos.append[ramo]
    # Ramo es el indice del ramo
    def botarRamo(self, index):
        self.ramos.remove[ramo]
    def verRamos(self):
        for i in self.ramos:
            print(f"CODIGO: {color.BOLD}{i[0]}{color.RESET}\nNOMBRE: {i[1]}\nMODULOS: {i[2]}\n")
    def menu(self, Intranet):
        while True:
            print(f"Bienvenido {color.BOLD}{self.nombre}{color.RESET}!\n")
            opt = int(input("(1) Ver ramos inscritos\n(2) Inscribir ramo\n(3) Botar ramo\n(0) Salir\n:"))
            if opt == 1:
                self.verRamos()
            elif opt == 2:
                self.inscribirRamo()
            elif opt == 3:
                self.botarRamo()
            elif opt == 0:
                Intranet.logout()
                break
            else:
                print(f"[{color.FAIL}*{color.RESET}] Opcion no valida, intente nuevamente")
class Ramo:
    # datos es una tupla con (Codigo, modulos asociados)
    def __init__(self, datos, cantidadNotas):
        self.datos = datos
        self.cantidadNotas = cantidadNotas

class App:
    def __init__(self):
        self.user = None
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
            # next(reader)  # Saltar la primera fila de encabezados
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
                    if user[3] == "Estudiante":
                        self.user = self.makeEstudiante(user[0], user[1], user[4:])
                    elif user[3] == "Profesor":
                        print("DEBUG: Profesor")
                        self.user = self.makeProfesor(user[0], user[1], user[3:])
                    break
            if self.user == None: # Si no se encuentra el usuario
                self.clear()
                print("Usuario o contraseña incorrectos :(")

    def logout(self):
        self.rut = None
        self.passwd = None
    
    def makeEstudiante(self, rut, nombre, ramos):
        self.user = Estudiante(rut, nombre, ramos) # Se crea un objeto estudiante

    def makeProfesor(self, rut, nombre, ramos):
        self.user = Profesor(rut, nombre, ramos)

    def clear(self): # Función para limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        manager = Admin()
        #print(self.users)
        while True:
            print("------------- Simple Intranet! --------------\n")
            opt = int(input("(1) Iniciar Sesion\n(2) Salir\n:"))
            if opt == 1:
                self.login()
                if isinstance(self.user, Admin):
                     self.user.menu(self)

                else:
                    self.user.menu(self)
            elif opt == 2:
                print(f"[{color.OKGREEN}*{color.RESET}] {color.BLUE} Saliendo...{color.RESET}")
                break
            else:
                print("Opcion no valida, intente nuevamente")

intranet = App()
intranet.run()
