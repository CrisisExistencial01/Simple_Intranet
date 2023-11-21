import csv
import os
import getpass # Para ingresar contraseñas :D
class Admin:
    def CrearEstudiante(self):
        estudiante = Estudiante()
class Estudiante:
    def __init__(self, ramo):
        self.ramos = ramos
    def inscribirRamo(ramo):
        pass
class Ramo:
    def __init__(self, modulos, cantidadNotas, blabla):
        self.modulos = modulos
        self.cantidadNotas = cantidadNotas

class App:
    def __init__(self):
        self.users = LoadUsers()
        self.rut = None
        self.passwd = None
    def LoadUsers(self):
        with open('Data/Users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            users = list( tuple(row) for row in reader)
            return users
    def login(self):
        rut = input("Ingrese su rut: ")
        passwd = getpass.getpass("Ingrese su contraseña: ") # Asi la contraseña no se ve :D
        if user == "ADMIN" and passwd == "NIMDA":
            self.user = Admin()
        else:
            for user in self.users:
                if user[0] == rut and user[1] == passwd:
                    self.rut = rut
                    self.passwd = passwd
                    return True
            if self.user == None: # Si no se encuentra el usuario
                self.clear()
                print("Usuario o contraseña incorrectos :(")
    def logout(self):
        self.rut = None
        self.passwd = None
    def estudiante(self):
        e = Estudiante() # Se crea un objeto estudiante
    def clear(self): # Función para limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while True:
            self.login()

app = App()
app.run()
