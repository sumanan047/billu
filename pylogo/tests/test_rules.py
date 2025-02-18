from pylogo.rules import move_to, move_by, move_up, move_down, move_left, move_right, move_by_at_angle
from pylogo.agent import Agent
import pytest
import numpy as np

@pytest.fixture
def _agent():
    return Agent()

def test_move_to(_agent):
    _agent.register_rule('move_to', move_to)
    move_to(_agent, 5, 10)
    assert _agent.x_pos == 5
    assert _agent.y_pos == 10

def test_move_by(_agent):
    _agent.register_rule('move_by', move_by)
    move_by(_agent, 2, 3)
    assert _agent.x_pos == 2
    assert _agent.y_pos == 3

def test_move_up(_agent):
    _agent.register_rule('move_up',move_up)
    _agent.y_pos = 5
    move_up(_agent, 2)
    assert _agent.y_pos == 7

def test_move_down(_agent):
    _agent.register_rule('move_down',move_down)
    _agent.y_pos = 5
    move_down(_agent, 2)
    assert _agent.y_pos == 3

def test_move_left(_agent):
    _agent.register_rule('move_left',move_left)
    _agent.x_pos = 5
    move_left(_agent, 2)
    assert _agent.x_pos == 3

def test_move_right(_agent):
    _agent.register_rule('move_right', move_right)
    _agent.x_pos = 5
    move_right(_agent, 2)
    assert _agent.x_pos == 7

def test_move_by_at_angle(_agent):
    _agent.register_rule('move_by_at_angle', move_by_at_angle)
    move_by_at_angle(_agent, 1, np.pi/2)
    assert np.isclose(_agent.x_pos, 0.0, atol=1e-2)  # approximate value with tolerance of 0.01
    assert np.isclose(_agent.y_pos, 1.0, atol=1e-2)  # approximate value with tolerance of 0.01

