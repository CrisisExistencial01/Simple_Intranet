#from admin import Admin
from db import DB
from prettier import color
from usuarios import User, Estudiante, Profesor
color = color()
db = DB()
#color.printOK("Testeo de la clase Admin")
# ESTUDIANTES : ["rut", "nombre", "ramos"]
# PROFESORES : ["rut", "nombre", "ramos"]
# USUARIOS : ["rut", "password", "tipo"]
nombres = ["Armando Casas", "Juanito Alcachofa", "Pedro Picapiedra", "Pablo Marmol", "Pepito Piscina"]
test_usuarios = [
            ["12345678-9", "12345678-9", "Estudiante"], 
            ["65431", "65431", "Profesor"],
            ["76234523-1", "76234523-1", "Estudiante"],
            ["87346823-k", "87346823-k", "Estudiante"],
            ["283672835-0", "283672835-0", "Profesor"],
            ]
def testFind():
    print("Testeando find")
    filtro = {"rut":"12345678-9"}
    print("Indice para '12345678-9' en users: ", db.find('users', filtro))
    print("en Estudiantes: ", db.find("estudiantes", filtro))
    print("en Profesores: ", db.find("profesores", filtro))
    print("Bucle de usuarios")
    for usuario in test_usuarios:
        print("Indice para ", usuario[0], " en users: ", db.find('users', {"rut":usuario[0]}))
        print("en Estudiantes: ", db.find("estudiantes", {"rut":usuario[0]}))
        print("en Profesores: ", db.find("profesores", {"rut":usuario[0]}))
def crear_usuarios():
    color.printBlue("Creando usuarios de prueba")
    #u = list(User(i[0], i[1], n, i[2]) for i, n in test_usuarios, nombres)
    u = list((User(i[0], i[1], n, i[2]) for i, n in zip(test_usuarios, nombres)))
    e = list((Estudiante(u[0], n, []) for u, n in zip(test_usuarios, nombres)))
    p = list((Profesor(u[0], n, []) for u, n in zip(test_usuarios, nombres)))

    for usuario, estudiante, profesor in zip(u, e, p):
        print("Users: ", db.create('users', usuario, "rut"))
        print("Estudiantes: ", db.create("estudiantes", estudiante, "rut"))
        print("Profesores: ", db.create("profesores", profesor, "rut"))
def create_user():
    filtro = {"rut":"98632-k"}
    print("Creando usuario")
    pepe = User("98632-k", "98632-k", "PEPE GRILLO", "Estudiante")
    db.create("users", pepe, "rut")
# acceso_db()
testFind()
#crear_usuarios()
create_user()
#print(crear_usuarios())
