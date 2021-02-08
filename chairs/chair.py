"""Implementation of Chair Class."""
from typing import List

from chairs import Espaldar
from chairs import Material


class Chair:
    """Class that allows to create Chairs."""
    def __init__(self, espaldar: Espaldar, material: Material, patas: List[str]) -> None:
        """Constructor for chair.

        Args:
            espaldar: (Espaldar) a espaldar for the chair.
            material: (Material) a material for the chair.
            patas: (List(str)) for the chair.
        """
        self.espaldar = espaldar
        self.material = material
        self.patas = patas

    def __str__(self) -> str:
        """String representation of espaldar.

        Returns:
            str: The name of the espaldar.
        """
        return f'{self.material}'

    def __repr__(self) -> str:
        """Repr of espaldar.

        Returns:
            str: The representation of the material.
        """
        return f'Chair of material {self.material}'

    def __len__(self) -> int:
        """Len of legs of the chair.

        Returns:
            int: amount of legs.
        """
        return len(self.patas)
