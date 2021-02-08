# skipping docs to skip on .pylintrc
"""Implementation of Espaldar Class."""
from chairs.material import Material


class Espaldar:
    """class that allows to create Espaldares."""

    def __init__(self, material: Material, color: str):
        """Constructor of the Espaldar Class.

        Args:
            material: (Material) a Material instance.
            color: (str) a color for the espaldar.
        """
        self.material = material
        self.color = color

    def __str__(self):
        """String representation of espaldar.

        Returns:
            str: The name of the espaldar.
        """
        return f'{self.material} - {self.color}'

    def __repr__(self):
        """Repr of espaldar.

        Returns:
            str: The representation of the material.
        """
        return f'Espaldar of material {self.material} and color {self.color}'
