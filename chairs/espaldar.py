# skipping docs to skip on .pylintrc
import pandas as pd

from chairs.material import Material


class Espaldar:
    """class that allows to create Espaldares"""
    def __init__(self, material: Material, color: str):
        self.material = material
        self.color = color

    def __str__(self):
        return f'{self.material} - {self.color}'

    def __repr__(self):
        return f'Espaldar of material {self.material} and color {self.color}'

