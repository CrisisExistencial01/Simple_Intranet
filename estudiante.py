import admin
import Innotes.color as color
manager = admin.Admin()
class Estudiante:
    def __init__(self, rut, nombre, ramos):
        self.rut = rut
        self.nombre = nombre
        self.ramos = ramos
    # Funciones binarias, se van a usar y validar en la app
    def inscribir_ramo(self, ramo):
        self.ramos.append(ramo)
        resultado = manager.update(path_Estudiantes, self.rut, self)
        if resultado:
            return True
        else:
            return False
    def desinscribir_ramo(self, ramo):
        self.ramos.remove(ramo)
        resultado = manager.update(path_Estudiantes, self.rut, self)
        if resultado:
            return True
        else:
            return False
    def ver_ramos(self):
        color.printOK("Ramos inscritos")
        manager.show(self.ramos)

    def ver_notas(self):
        color.printOK("Notas")
        for ramo in self.ramos:
            print(f"{ramo.nombre}: {ramo.nota}")
    def menu(self):
        print(f"Bienvenido {self.nombre}")
        print("Seleccione una opcion: ")
        print("(1) Inscribir ramo")
        print("(2) Desinscribir ramo")
        print("(3) Ver ramos inscritos")
        print("(4) Ver notas")
        print("(0) Salir")
        opcion = int(input("Opcion: "))
        if opcion == 0:
            print("Gracias por usar Innotes")
            color.printOKBLUE("Saliendo ...")
        elif opcion == 1:
            self.inscribir_ramo()
        elif opcion == 2:
            self.desinscribir_ramo()
        elif opcion == 3:
            self.ver_ramos()
        elif opcion == 4:
            self.ver_notas()
        else:
            color.printFail("Opcion invalida")
