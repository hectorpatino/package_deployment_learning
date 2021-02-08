# skipping docs to skip on .pylintrc
"""Implementation of Espaldar Class."""
from typing import Optional

from chairs.material import Material


class Espaldar:
    """class that allows to create Espaldares."""

    def __init__(self, material: Material, color: Optional[str] ='Black') -> None:
        """Constructor of the Espaldar Class.

        Args:
            material: (Material) a Material instance.
            color: (str, optional) a color for the espaldar. Defaults to Black.
        """
        self.material = material
        self.color = color

    def __str__(self) -> str:
        """String representation of espaldar.

        Returns:
            str: The name of the espaldar.
        """
        return f'{self.material} - {self.color}'

    def __repr__(self) -> str:
        """Repr of espaldar.

        Returns:
            str: The representation of the material.
        """
        return f'Espaldar of material {self.material} and color {self.color}'
