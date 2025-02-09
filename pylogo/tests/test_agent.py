import pytest
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pylogo.agent import Agent, AgentSet
from pylogo.distributions import Distribution_2D


def test_agent_creation():
    agent = Agent()
    assert agent.unique_id is not None
    assert agent.color == (1, 0, 0)
    assert agent.position == (0, 0)
    assert agent.size == (1, 1)

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

def test_agentset_creation():
    agent_set = AgentSet()
    assert isinstance(agent_set, AgentSet)
    assert len(agent_set) == 100