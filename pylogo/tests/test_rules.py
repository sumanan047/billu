from pylogo.rules import move_to, move_by, move_up, move_down, move_left, move_right, move_by_at_angle
from pylogo.distributions import Distribution_1D, Distribution_2D
from pylogo.agent import Agent, AgentSet
import pytest
import numpy as np

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
