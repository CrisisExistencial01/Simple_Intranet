
class User:
    def __init__(self, rut, password, nombre, tipo):
        self.rut = rut
        self.password = password
        self.nombre = nombre
        self.tipo = tipo
        self.nombre = nombre
    def get(self, attr):
        return getattr(self, attr, None)
    def set(self, attr, value):
        setattr(self, attr, value)
    def to_list(self):
        return [self.rut, self.password, self.nombre, self.tipo]
class Estudiante:
    def __init__(self, rut, nombre, ramos):
        self.rut = rut
        self.nombre = nombre
        self.ramos = ramos
    def get(self, attr):
        return getattr(self, attr, None)
    def set(self, attr, value):
        setattr(self, attr, value)
    def to_list(self):
        return [self.rut, self.nombre, self.ramos]
class Profesor:
    def __init__(self, rut, nombre, ramos):
        self.rut = rut
        self.nombre = nombre
        self.ramos = ramos
    def get(self, attr):
        return getattr(self, attr, None)
    def set(self, attr, value):
        setattr(self, attr, value)
    def to_list(self):
        return [self.rut, self.nombre, self.ramos]
