import pytest
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
    print(type(agent.sprite))
    assert agent.sprite is not None