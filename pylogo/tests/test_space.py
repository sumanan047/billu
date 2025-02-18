import pytest
from pylogo.space import Space

class MockModel:
    pass


class MockRule:
    pass

def test_space_initialization():
    space = Space()
    assert space.x_min == 0
    assert space.x_max == 1
    assert space.y_min == 0
    assert space.y_max == 1
    assert space.color == (1, 1, 0)

def test_space_set_space():
    space = Space()
    space.set_space(energy = 100)
    assert space.properties['energy'] == 100


def test_space_register_model():
    space = Space()
    model = MockModel()
    space.register_model(model)
    assert space.model == model

def test_space_register_rule():
    space = Space()
    rule = MockRule()
    space.register_rule(rule)
    assert rule in space.rules

def test_space_visualize():
    space = Space()
    space._visualize()
    # assert that the file space.png is created