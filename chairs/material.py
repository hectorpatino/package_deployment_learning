"""This module allows to instantiate a material for a chair componente."""


class Material:
    """Class that creates the material of a component of the chair."""
    def __init__(self, nombre: str):
        """Constructor of Material Class.

        Args:
            nombre: (str) name of the material.

        Raises:
            TypeError: if `nombre`is not a string.
        """
        if not isinstance(nombre, str):
            raise TypeError('nombre must be a string')
        self.nombre = nombre

    def __str__(self):
        """String representation of Material.

        Returns:
            str: The name of the material.
        """
        return self.nombre

    def __repr__(self):
        """Repr of Material.

        Returns:
            str: The representation of the material.
        """
        return f'Material of type {self.nombre}'
