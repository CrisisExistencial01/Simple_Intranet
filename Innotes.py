import csv
from admin import Admin

# PATHS
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
        print(f"[{col.or.OKGREEN}*{color.RESET}] {texto}")
    def printFail(self, texto):
        print(f"[{color.FAIL}*{color.RESET}] {texto}")
    def printWarning(self, texto):
        print(f"[{color.WARNING}*{color.RESET}] {texto}")
    def printOKBlue(self, texto):
        print(f"[{color.OKGREEN}*{color.RESET}] {color.BLUE}{texto}{color.RESET}")
    def bold(self, texto):
        return f"{color.BOLD}{texto}{color.RESET}"

class App:
    def __init__():
        # Variables utiles
        self.user = None
        self.manager = Admin()
        self.rut = None
        self.password = None
        # Usuarios
        self.users = self.manager.loadFile(path_Usuarios)
        self.estudiantes = self.manager.loadFile(path_Estudiantes)
        self.profesores = self.manager.loadFile(path_Profesores)
        # Ramos
        self.ramos = self.manager.loadFile(path_Ramos)
    # Funciones de la app
    def login(self, rut, password):
        for user in self.users:
            if user[0] == self.rut and user[1] == self.password:
                self.user = user
                return True
        return False
    def run(self):
        
