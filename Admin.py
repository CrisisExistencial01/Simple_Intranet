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
        l = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        for dato in l:
            if data == data:
                search = l.index(dato)
                l[search] = new
        self.saveList(path, l)
    def add(self, path, data):
        # Agrega un dato a un archivo csv
        l = self.loadFile(path)
        # l es la lista de tuplas retornadas por loadFile()
        l.append(data)
        self.saveList(path, l)
        return l # retorna la lista actualizada
    # ADMINISTRACION DE USUARIOS
    def addUser(self, Intranet):
        rut = input("Rut del nuevo usuario: ")
        nombre = input("Nombre del nuevo usuario: ")
        rol = input("Seleccione el tipo de usuario: \n(1) Estudiante\n(2) Profesor: ")
        l = []
        if rol == "1":
            user = (rut, rut, nombre, "Estudiante")
            data = (rut, nombre, l[0:])
            Intranet.estudiantes.append(data)
            self.save(path_Estudiantes, data)
        elif rol == "2":
            user = (rut, rut, nombre, "Profesor")
            data = (rut, nombre, l[0:])
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
            print(f"[{color.FAIL}*{color.RESET}]Opción no válida, intente nuevamente")
              
