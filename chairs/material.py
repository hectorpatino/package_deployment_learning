"""This module allows to instantiate a material for a chair componente"""


class Material:
    """Class that creates the material of a component of the chair"""
    def __init__(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError('nombre must be a string')
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return f'Material of type {self.nombre}'
