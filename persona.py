from abc import ABCMeta, abstractmethod

class persona(metaclass=ABCMeta):

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def saludar(self):
        pass