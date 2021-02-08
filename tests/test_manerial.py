import pytest

from chairs import Espaldar
from chairs import Material


def test_material_init():
    material = Material('wood')
    assert material.nombre == 'wood'
    assert str(material) == 'wood'


def test_wrong_material_init():
    with pytest.raises(TypeError):
        material = Material(5)


def test_espaldar_init():
    material = Material('wood')
    espaldar = Espaldar(material, 'red')
    assert espaldar.material.nombre == material.nombre
    assert str(espaldar) == 'wood - red'
    assert repr(espaldar) == 'Espaldar of material wood and color red'


