import pytest
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pylogo.agent import Agent, AgentSet, TupleDescriptor
from pylogo.distributions import Distribution_2D, Distribution_1D

# fixtures for testing

@pytest.fixture
def dist1():
    d1 = Distribution_2D()
    d1.uniform([0,0], [1,10], 100)
    return d1

@pytest.fixture
def dist2():
    d2 = Distribution_2D()
    d2.uniform([0.5, 0.5],[0.5,0.5], 100)
    return d2

@pytest.fixture
def dist3():
    d3 = Distribution_1D()
    d3.uniform(90,90, 100)
    return d3

@pytest.fixture
def dist4():
    d4 = Distribution_2D()
    d4.uniform([0,0],[1,1], 10)
    return d4

# test for TupleDescriptor ==============================================
def test_tuple_descriptor_get():
    class TestAgent:
        color = TupleDescriptor()

    agent = TestAgent()
    agent.color = (1, 0)
    assert agent.color == (1, 0)

def test_tuple_descriptor_set():
    class TestAgent:
        position = TupleDescriptor()

    agent = TestAgent()
    with pytest.raises(ValueError):
        agent.position = (1, 2)

def test_tuple_descriptor_set_invalid_type():
    class TestAgent:
        position = TupleDescriptor()

    agent = TestAgent()
    with pytest.raises(TypeError):
        agent.position = "1, 2"


# test for Agent ========================================================
def test_agent_creation():
    agent = Agent()
    assert agent.unique_id is not None
    assert isinstance(agent.unique_id, str)
    assert agent.color == (1, 0, 0)
    assert agent.position == (0, 0)
    assert agent.size == (1, 1)
    assert agent._r_color == 1
    assert agent._g_color == 0
    assert agent._b_color == 0
    assert agent.x_pos == 0
    assert agent.y_pos == 0
    assert agent.x_size == 1
    assert agent.y_size == 1
    assert agent.properties == {}
    assert agent.sprite is not None
    assert agent.agent_dict['unique_id'][0] == agent.unique_id

def test_agent_creation_bad_color():
    with pytest.raises(ValueError):
        agent = Agent(color=(1, 0, 2))

def test_agent_patch():
    agent = Agent()
    assert isinstance(agent.sprite, mpl.patches.Rectangle)

def test_agent_set_properties_int():
    agent = Agent()
    agent.set_properties(age=90)
    assert agent.properties['age'] == 90

def test_agent_set_properties_str():
    agent = Agent()
    agent.set_properties(name='John')
    assert agent.properties['name'] == 'John'

def test_agent_set_properties_int_list():
    agent = Agent()
    agent.set_properties(cars = ['mercedez', 'volvo', 'ferrari'])
    assert agent.properties['cars'] == ['mercedez', 'volvo', 'ferrari']

def test_agentset_creation_failure():
    with pytest.raises(ValueError):
        agent_set = AgentSet(10)

def test_agentset_creation(dist1, dist2):
    agent_set = AgentSet(number=100, position_dist=dist1, size_dist=dist2)
    assert isinstance(agent_set, AgentSet)
    assert len(agent_set) == 100

def test_agentset_creation_properties_failure(dist1, dist2):
    with pytest.raises(TypeError):
        agent_set = AgentSet(number=100, position_dist=dist1, size_dist=dist2, age = [1,2,3])

def test_agentset_creation_properties(dist1, dist2, dist3):
    agent_set = AgentSet(number=100, position_dist=dist1, size_dist=dist2, age=dist3)
    assert isinstance(agent_set, AgentSet)
    assert len(agent_set) == 100
    # the distribution is a constant
    for agent in agent_set:
        assert agent.properties['age'] == 90

def test_agentset_creation_properties_failure_different_size_dist(dist4, dist2, dist3):
    with pytest.raises(ValueError):
        agent_set = AgentSet(number=100, position_dist=dist4, size_dist=dist2, age=dist3)