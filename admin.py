import csv
from db import DB
path_Usuarios = "Data/Users/Users.csv"
path_Estudiantes = "Data/Users/Estudiantes.csv"
path_Profesores = "Data/Users/Profesores.csv"
path_Ramos = "Data/Ramos/Ramos.csv"
db = DB()

class Usuario:
    def __init__(self, rut, password, nombre, rol):
        self.rut = rut
        self.password = password
        self.nombre = nombre
        self.rol = rol
    def getRut(self):
        return self.rut
    def getPassword(self):
        return self.password
    def getNombre(self):
        return self.nombre
    def getRol(self):
        return self.rol
class Admin:
    # ADMINISTRACION DE ARCHIVOS CSV
    # Ya no es necesario el manejo de archivos desde admin.py
    def find(self, parametro , lista):
        for i in lista: # i es una tupla
            if i[0] == parametro:
                return lista.index(i)
    def findInObject(self, parametro, lista):
        for i in lista:
            if i.rut == parametro:
                return lista.index(i)
    def loadFile(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data # data es una lista de tuplas
    def save(self, path, data):
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    def saveList(self, path, data):
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    def show(self, lista):
        for i in lista:
            print(i)
    def delete(self, path, data):
        # Elimina un dato de un archivo csv
        lista = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        for ramo in lista:
            if ramo == data:
                l.pop(ramo)
        self.saveList(path, lista)
    def update(self, path, data, new):
        # Actualiza un dato de un archivo csv
        lista = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        for dato in lista:
            if data == data:
                search = lista.index(dato)
                lista[search] = new
        self.saveList(path, lista)
        if lista[search] == new:
            return True 
        else:
            return False
    def add(self, path, data):
        # Agrega un dato a un archivo csv
        lista = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        lista.append(data)
        self.saveList(path, lista)
        return l # retorna la lista actualizada
    # ADMINISTRACION DE USUARIOS
    def addUser(self, ):

    def addUser(self, Intranet):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: ")
        ramos = []
        if rol == "1":
            user = (rut, rut, nombre, "Estudiante")
            data = (rut, nombre, ramos[0:])
            self.add(path_Estudiantes, data)
        elif rol == "2":
            user = (rut, rut, nombre, "Profesor")
            data = (rut, nombre, ramos[0:])
            self.add(path_Profesores, data)
        else:
            print("Opción no válida, intente nuevamente")
        Intranet.users.append(user)
        self.save(path_Usuarios, user)
        color.printOK("Usuario agregado exitosamente")

    def deleteUser(self, Intranet):
        rut = input("Ingrese el rut del usuario a eliminar: ")
        user = self.find(rut, Intranet.users) # retorna el indice del usuario en la lista
        if user == None:
            #print(f"[{color.FAIL}*{color.RESET}] Usuario no encontrado")
            color.printFail("Usuario no encontrado")
        else:
            self.delete(path_Usuarios, Intranet.users[user])
            print(f"[{color.OKGREEN}*{color.RESET}] Usuario eliminado exitosamente")
    def updateUser(self, Intranet):
        rut = input("Ingrese el rut del usuario a actualizar: ")
        user = self.find(rut, Intranet.users)
        if user == None:
            color.printFail("Usuario no encontrado")
        else:
            opt = int(input("Seleccione el dato a actualizar: \n(1) Rut\n(2) Nombre: \n(3)contraseña:\n(4) Tipo de usuario: "))
            if opt == 1:
                nuevo_rut = input("Ingrese el nuevo rut del usuario: ")
                if Intranet.users[user][3] == "Estudiante":
                    ans = self.update(path_Estudiantes, Intranet.estudiantes[user][0], nuevo_rut)
                elif Intranet.users[user][3] == "Profesor":
                    ans = self.update(path_Profesores, Intranet.profesores[user][0], nuevo_rut)
                ans2 = self.update(path_Usuarios, Intranet.users[user][0], nuevo_rut)
                if ans == True and ans2 == True:
                    Intranet.users[user][0] = rut
                    color.printOK("Usuario actualizado exitosamente")
                else:
                    color.printFail("Usuario no encontrado")

            elif opt == 2:
                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                ans = self.update(path_Estudiantes, Intranet.estudiantes[user][1], nombre)
                ans2 = self.update(path_Usuarios, Intranet.users[user][2], nombre)
                if ans == True and ans2 == True:
                    Intranet.users[user][2] = nombre
                    Intranet.estudiantes[user][1] = nombre
                    color.printOK("Usuario actualizado exitosamente")
                else:
                    color.printFail("Usuario no encontrado")
            elif opt == 3:
                password = input("Ingrese la nueva contraseña del usuario: ")
                Intranet.users[user][1] = password
                self.saveList(path_Usuarios, Intranet.users)
                color.printOK("Usuario actualizado exitosamente")
            elif opt == 4:
                rol = input("Ingrese el nuevo tipo de usuario: ")
                Intranet.users[user][3] = rol
                self.saveList(path_Usuarios, Intranet.users)
                color.printOK("Usuario actualizado exitosamente")
            else:
                color.printFail("Opción no válida, intente nuevamente")
    def menu(self, Intranet):
        while True:
            sel = input("Seleccione una opción: \n(1) Agregar usuario\n(2) Eliminar usuario\n(3) Actualizar usuario\n(4) Mostrar usuarios\n(0) Salir\n ")
            if sel == "1":
                self.addUser(Intranet)
            elif sel == "2":
                self.deleteUser(Intranet)
            elif sel == "3":
                self.updateUser(Intranet)
            elif sel == "4":
                self.show(Intranet.users)
            elif sel == "0":
                break
            else:
                color.printFail("Opción no válida, intente nuevamente")
