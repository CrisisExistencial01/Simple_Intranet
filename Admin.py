import csv

path_Usuarios = "Data/Users/Users.csv"
path_Estudiantes = "Data/Users/Estudiantes.csv"
path_Profesores = "Data/Users/Profesores.csv"
path_Ramos = "Data/Ramos/Ramos.csv"
class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def printOK(self, texto):
        print(f"[{color.OKGREEN}*{color.RESET}] {texto}")
    def printFail(self, texto):
        print(f"[{color.FAIL}*{color.RESET}] {texto}")
    def printWarning(self, texto):
        print(f"[{color.WARNING}*{color.RESET}] {texto}")
    def printBlue(self, texto):
        print(f"[{color.BLUE}*{color.RESET}] {texto}")
color = color()
class Admin:
    # ADMINISTRACION DE ARCHIVOS CSV
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
        l = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        for ramo in l:
            if ramo == data:
                l.pop(ramo)
        self.saveList(path, l)
    def update(self, path, data, new):
        # Actualiza un dato de un archivo csv
        lista = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        for dato in lista:
            if data == data:
                search = lista.index(dato)
                lista[search] = new
        self.saveList(path, lista)
    def add(self, path, data):
        # Agrega un dato a un archivo csv
        lista = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        l.append(data)
        self.saveList(path, l)
        return l # retorna la lista actualizada
    # ADMINISTRACION DE USUARIOS
    def addUser(self, Intranet):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: ")
        lista = []
        if rol == "1":
            user = (rut, rut, nombre, "Estudiante")
            data = (rut, nombre, lista[0:])
            Intranet.estudiantes.append(data)
            self.save(path_Estudiantes, data)
        elif rol == "2":
            user = (rut, rut, nombre, "Profesor")
            data = (rut, nombre, lista[0:])
            Intranet.profesores.append(data)
            self.save(path_Profesores, data)
        else:
            print("Opción no válida, intente nuevamente")
        Intranet.users.append(user)
        self.save(path_Usuarios, user)
        print(f"[{color.OKGREEN}*{color.RESET}]Usuario agregado exitosamente")
    def addUser(self, Intranet):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = int(input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: "))
        if rol == 1:
            user = (rut, rut, nombre, "Estudiante")
            Intranet.estudiantes.append(user)
            self.save(path_Estudiantes, user)
            Intranet.users.append(user)
            self.save(path_Usuarios, user)
            print(f"[{color.OKGREEN}*{color.RESET}]Usuario agregado exitosamente")

        elif rol == 2:
            user = (rut, rut, nombre, "Profesor")
            Intranet.profesores.append(user)
            self.save(path_Profesores, user)
            Intranet.users.append(user)
            self.save(path_Usuarios, user)
            print(f"[{color.OKGREEN}*{color.RESET}]Usuario agregado exitosamente")

        else:
            print(f"[{color.FAIL}*{color.RESET}] Opción no válida, intente nuevamente")
    def deleteUser(self, Intranet):
        rut = input("Ingrese el rut del usuario a eliminar: ")
        user = self.find(rut, Intranet.users)
        if user == None:
            #print(f"[{color.FAIL}*{color.RESET}] Usuario no encontrado")
            color.printFail("Usuario no encontrado")
        else:
            Intranet.users.pop(user)
            self.saveList(path_Usuarios, Intranet.users)
            print(f"[{color.OKGREEN}*{color.RESET}] Usuario eliminado exitosamente")
    def updateUser(self, Intranet):
        rut = input("Ingrese el rut del usuario a actualizar: ")
        user = self.find(rut, Intranet.users)
        if user == None:
            print(f"[{color.FAIL}*{color.RESET}] Usuario no encontrado")
        else:
            opt = int(input("Seleccione el dato a actualizar: \n(1) Rut\n(2) Nombre: \n(3)contraseña:\n(4) Tipo de usuario: "))
            if opt == 1:
                rut = input("Ingrese el nuevo rut del usuario: ")
                Intranet.users[user][0] = rut
                self.saveList(path_Usuarios, Intranet.users)
                print(f"[{color.OKGREEN}*{color.RESET}] Usuario actualizado exitosamente")
            elif opt == 2:
                nombre = input("Ingrese el nuevo nombre del usuario: ")
                Intranet.users[user][2] = nombre
                self.saveList(path_Usuarios, Intranet.users)
                print(f"[{color.OKGREEN}*{color.RESET}] Usuario actualizado exitosamente")
            elif opt == 3:
                password = input("Ingrese la nueva contraseña del usuario: ")
                Intranet.users[user][1] = password
                self.saveList(path_Usuarios, Intranet.users)
                print(f"[{color.OKGREEN}*{color.RESET}] Usuario actualizado exitosamente")
            elif opt == 4:
                rol = input("Ingrese el nuevo tipo de usuario: ")
                Intranet.users[user][3] = rol
                self.saveList(path_Usuarios, Intranet.users)
                print(f"[{color.OKGREEN}*{color.RESET}] Usuario actualizado exitosamente")

