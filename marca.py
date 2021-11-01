class Marca:
    pass

    def __init__(self, nombre):
        self.__nombre = nombre

    def __int__(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre=nombre
