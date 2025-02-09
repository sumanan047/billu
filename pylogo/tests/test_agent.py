import pytest
from pylogo.agent import Agent, AgentSet
from pylogo.distributions import Distribution

def test_agent_creation():
    agent = Agent()
    assert agent.unique_id is not None
    assert agent.color == (1, 0, 0)
    assert agent.position == (0, 0)
    assert agent.size == (1, 1)

def test_agent_register_model():
    agent = Agent()
    model = object()
    agent.register_model(model)
    assert agent.model is model

def test_agent_register_rule():
    agent = Agent()
    rule = object()
    agent.register_rule(rule)
    assert rule in agent.rules

def test_agentset_creation():
    agent_set = AgentSet()
    assert agent_set.position_dist is None
    assert agent_set.size_dist is None
    assert agent_set.color is None

def test_agentset_make_agents():
    distribution = Distribution()
    distribution.uniform(low=[-10, -10], high=[10, 10], size=100)
    agent_set = AgentSet(number=100)
    agent_set.position_dist = distribution
    agents = agent_set.make_agents()
    assert len(agents) == 100
    for agent in agents:
        assert isinstance(agent, Agent)

def test_agentset_register_model():
    agent_set = AgentSet()
    model = object()
    agent_set.register_model(model)
    assert agent_set.model is model

def test_agentset_register_rule():
    agent_set = AgentSet()
    rule = object()
    agent_set.register_rule(rule)
    assert rule in agent_set.rules

def test_agent_position_setter():
    agent = Agent()
    agent.position = (0.5, 0.5)
    assert agent.position == (0.5, 0.5)