import csv
from ramos import Ramo
from usuarios import User, Estudiante, Profesor
# PATHS
path_Usuarios = "Data/Users/Users.csv"
path_Estudiantes = "Data/Users/Estudiantes.csv"
path_Profesores = "Data/Users/Profesores.csv"
path_Ramos = "Data/Ramos/Ramos.csv"
path_Notas = "Data/Ramos/Notas.csv"
# CLASES

class DB:
    def __init__(self):
        self.load_data()
    def loadFile(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    def load_data(self):
        users = list(User(i[0], i[1], i[2], i[3]) for i in self.loadFile(path_Usuarios))
        estudiantes = list(Estudiante(i[0], i[1], i[2:]) for i in self.loadFile(path_Estudiantes))
        profesores = list(Profesor(i[0], i[1], i[2:]) for i in self.loadFile(path_Profesores))
        ramos = list(Ramo(i[0], i[1], i[2]) for i in self.loadFile(path_Ramos))
        # notas = 
        # Ahora se guardan los datos en un diccionario
        # cada llave del diccionario es un modelo, y cada valor es una lista de objetos
        self.datos = {
            "users": users,
            "estudiantes": estudiantes,
            "profesores": profesores,
            "ramos": ramos
            #"notas": notas
                }
        self.paths = {
            "users": path_Usuarios,
            "estudiantes": path_Estudiantes,
            "profesores": path_Profesores,
            "ramos": path_Ramos
                }
    def save(self, path, data): # se usa para AGREGAR un dato adicional a un csv
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def saveList(self, path, data): # se usa para GUARDAR TODOS los datos de un csv
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    

    def update(self, modelo, filtro, objeto):
        # Actualiza un dato de un archivo csv
        coleccion = self.datos[modelo] 
        path = self.paths[modelo]
        indice = self.find(coleccion, filtro)
        coleccion[indice] = objeto
        self.datos[modelo] = coleccion
        self.saveList(path, coleccion)

    def find(self, modelo, filtro):
        # filtro es un diccionario de la forma: {"atributo objeto": "valor"}
        coleccion = self.datos[modelo]
        for objeto in coleccion:
            coincidencia = True
            for key, value in filtro.items():
                attr = getattr(objeto, key, None)
                if attr != value:
                    coincidencia = False
                    break

            if coincidencia:
                return coleccion.index(objeto)
        return -1
    # getters
    def getRamos(self):
        return self.datos["ramos"]
    def getEstudiantes(self):
        return self.datos["estudiantes"]
    def getProfesores(self):
        return self.datos["profesores"]
    def getUsers(self):
        return self.datos["users"]
    # CRUD:
    def create(self, modelo, objeto, attr):
        # Crea un objeto en un archivo csv
        coleccion = self.datos[modelo]
        print("DEBUG:", coleccion)
        filtro = {attr: getattr(objeto, attr, None)}
        print("DEBUG:", filtro)
        if coleccion is None:
            print(f"El modelo '{modelo}' no existe en los datos")
            return False

        print(f"El modelo '{modelo}' existe en los datos")
        print(f"Colección de objetos: {coleccion}")
        for obj in coleccion:
            print(f"Tipo de objeto en la colección: {type(obj)}")
        if self.find(coleccion, filtro) != -1:
            print(f"El objeto '{objeto}' ya existe en la colección")
             
            path = self.paths[modelo]
            coleccion.append(objeto) # se agrega el objeto a la lista
            self.datos[modelo] = coleccion

            data = objeto.to_list() # se convierte el objeto a una lista guardable en csv

            self.save(path, data) # se guarda el objeto en el csv
            return True
        else:
            return False

    def delete(self, lista, data):
        # Elimina un dato de un archivo csv
        for t in lista: # donde t es una tupla
            if t == data:
                lista.pop(t)
        self.saveList(path, lista)

