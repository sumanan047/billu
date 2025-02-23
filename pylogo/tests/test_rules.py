from pylogo.rules import *
from pylogo.distributions import Distribution_1D, Distribution_2D
from pylogo.agent import Agent, AgentSet
import pytest
import numpy as np
import math

@pytest.fixture
def _agent():
    return Agent()

@pytest.fixture
def _agent_set():
    NO_AGENTS = 5
    d1 = Distribution_2D()
    d1.uniform(low=[-20,-20], high=[50,70], size=NO_AGENTS)

    d2 = Distribution_2D()
    d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=NO_AGENTS)
    return AgentSet(number=5,position_dist=d1,size_dist=d2)

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


#now testing for AgentSet
def test_move_to_agentset(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_to', move_to)
    move_to(agent_set, 5, 10)
    assert agent_set[0].x_pos == 5
    assert agent_set[0].y_pos == 10

def test_move_up_agentset(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_up', move_up)
    agent_set[0].y_pos = 5
    move_up(agent_set, 2)
    assert agent_set[0].y_pos == 7

def test_move_down_agentset(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_down', move_down)
    agent_set[0].y_pos = 5
    move_down(agent_set, 2)
    assert agent_set[0].y_pos == 3

def test_move_left_agentset(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_left', move_left)
    agent_set[0].x_pos = 5
    move_left(agent_set, 2)
    assert agent_set[0].x_pos == 3

def test_move_right_agentset(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_right', move_right)
    agent_set[0].x_pos = 5
    move_right(agent_set, 2)
    assert agent_set[0].x_pos == 7

def test_move_by_at_angle_agentset(_agent_set):
    agent_set = _agent_set
    # get initial x and y positions of first agent
    x_pos = agent_set[0].x_pos
    y_pos = agent_set[0].y_pos
    for agent in agent_set:
        agent.register_rule('move_by_at_angle', move_by_at_angle)
    move_by_at_angle(agent_set, 1, np.pi/2)
    # check if the first agent has moved by 1 unit in the y direction
    assert np.isclose(agent_set[0].x_pos - x_pos, 0.0, atol=1e-2)  # approximate value with tolerance of 0.01
    assert np.isclose(agent_set[0].y_pos - y_pos, 1.0, atol=1e-2)  # approximate value with tolerance of 0.01

def test_move_randomly(_agent_set):
    agent_set = _agent_set
    # get first agent's original x and y positions
    x_pos = agent_set[0].x_pos
    y_pos = agent_set[0].y_pos
    for agent in agent_set:
        agent.register_rule('move_randomly', move_randomly)
    move_randomly(agent_set)
    assert agent_set[0].x_pos != x_pos
    assert agent_set[0].y_pos != y_pos

# test for ValueError
def test_move_to_value_error():
    with pytest.raises(ValueError):
        move_to("agent", 1, 2)

def test_move_by_value_error():
    with pytest.raises(ValueError):
        move_by("agent", 1, 2)

def test_move_up_value_error():
    with pytest.raises(ValueError):
        move_up("agent", 1)

def test_move_down_value_error():
    with pytest.raises(ValueError):
        move_down("agent", 1)

def test_move_left_value_error():
    with pytest.raises(ValueError):
        move_left("agent", 1)

def test_move_right_value_error():
    with pytest.raises(ValueError):
        move_right("agent", 1)

def test_move_by_at_angle_value_error():
    with pytest.raises(ValueError):
        move_by_at_angle("agent", 1, 2)

def test_move_randomly_value_error():
    with pytest.raises(ValueError):
        move_randomly("agent", [0,1], [0,1])

def test_move_to_agentset_value_error():
    with pytest.raises(ValueError):
        move_to("agent", 1, 2)

def test_move_up_agentset_value_error():
    with pytest.raises(ValueError):
        move_up("agent", 1)

def test_move_down_agentset_value_error():
    with pytest.raises(ValueError):
        move_down("agent", 1)

def test_move_left_agentset_value_error():
    with pytest.raises(ValueError):
        move_left("agent", 1)

def test_move_right_agentset_value_error():
    with pytest.raises(ValueError):
        move_right("agent", 1)

def test_move_by_at_angle_agentset_value_error():
    with pytest.raises(ValueError):
        move_by_at_angle("agent", 1, 2)

def test_move_randomly_agentset_value_error():
    with pytest.raises(ValueError):
        move_randomly("agent", [0,1], [0,1])

def test_update_property(_agent):
    # NOTE: setting properties work but the new method update_property is not working
    _agent.set_properties(age=5)
    _agent.register_rule('update_property', update_property)
    update_property(_agent, 'age', 10)
    assert _agent.agent_dict['age'] == 10

def test_update_property_value_error():
    with pytest.raises(ValueError):
        update_property("agent", 'age', 10)

def test_update_property_key_error(_agent):
    _agent.set_properties(age=5)
    _agent.register_rule('update_property', update_property)
    with pytest.raises(KeyError):
        update_property(_agent, 'height', 10)

def test_increment_property(_agent):
    _agent.set_properties(age=5)
    _agent.register_rule('increment_property', increment_property)
    increment_property(_agent, 'age', 5)
    assert _agent.agent_dict['age'] == 10

def test_decrement_property(_agent):
    _agent.set_properties(age=5)
    _agent.register_rule('decrement_property', decrement_property)
    decrement_property(_agent, 'age', 5)
    assert _agent.agent_dict['age'] == 0

def test_increment_property_value_error():
    with pytest.raises(ValueError):
        increment_property("agent", 'age', 10)

def test_decrement_property_value_error():
    with pytest.raises(ValueError):
        decrement_property("agent", 'age', 10)

def test_increment_property_key_error(_agent):
    _agent.set_properties(age=5)
    _agent.register_rule('increment_property', increment_property)
    with pytest.raises(KeyError):
        increment_property(_agent, 'height', 10)

def test_move_randomly(_agent):
    _agent.register_rule('move_randomly', move_randomly)
    move_randomly(_agent, [0,1], [0,1])
    assert _agent.x_pos != 0
    assert _agent.y_pos != 0

def test_increment_property_agentset(_agent_set):
    agent_set = _agent_set
    agent_set.set_properties(age=5)
    for agent in agent_set:
        agent.register_rule('increment_property', increment_property)
    increment_property(agent_set, 'age', 5)
    assert agent_set[0].agent_dict['age'] == 10

def test_decrement_property_agentset(_agent_set):
    agent_set = _agent_set
    agent_set.set_properties(age=5)
    for agent in agent_set:
        agent.register_rule('decrement_property', decrement_property)
    decrement_property(agent_set, 'age', 5)
    assert agent_set[0].agent_dict['age'] == 0

def test_increment_property_agentset_value_error():
    with pytest.raises(ValueError):
        increment_property("agent", 'age', 10)

def test_update_property(_agent_set):
    agent_set = _agent_set
    agent_set.set_properties(age=5)
    for agent in agent_set:
        agent.register_rule('update_property', update_property)
    update_property(agent_set, 'age', 10)
    assert agent_set[0].agent_dict['age'] == 10

def test_move_ranomly(_agent_set):
    agent_set = _agent_set
    for agent in agent_set:
        agent.register_rule('move_randomly', move_randomly)
    move_randomly(agent_set, [0,1], [0,1])
    assert agent_set[0].x_pos != 0
    assert agent_set[0].y_pos != 0


def test_move_by(_agent_set):
    agent_set = _agent_set
    x_pos = agent_set[0].x_pos
    y_pos = agent_set[0].y_pos
    for agent in agent_set:
        agent.register_rule('move_by', move_by)
    move_by(agent_set, 2, 3)
    assert math.isclose(agent_set[0].x_pos - x_pos, 2, abs_tol=1e-9)
    assert math.isclose(agent_set[0].y_pos - y_pos, 3, abs_tol=1e-9)

def test_decrement_property_agentset_value_error():
    with pytest.raises(ValueError):
        decrement_property("agent", 'age', 10)

def test_decrement_property_agentset_key_error(_agent_set):
    agent_set = _agent_set
    agent_set.set_properties(age=5)
    for agent in agent_set:
        agent.register_rule('decrement_property', decrement_property)
    with pytest.raises(KeyError):
        decrement_property(agent_set, 'height', 10)