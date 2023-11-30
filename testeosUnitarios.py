from Admin import color
from Admin import Admin
color.printOK("Testeo de la clase Admin")
# testeos de la clase Admin
# 1. Crear un usuario
# 2. Crear un usuario con un nombre de usuario ya existente
# 3. Crear un usuario con un nombre de usuario vacio
# 4. Crear un usuario con un nombre de usuario con caracteres especiales
def crear_usuario():
    print("Creando un usuario")
    admin = Admin()
    admin.crear_usuario("admin", "admin", "admin", "admin", "admin", "admin")
    color.printOK("Usuario creado")


