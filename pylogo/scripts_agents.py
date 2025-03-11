import numpy as np
from pylogo.agent import Agent
from pylogo.agent import AgentSet

def loose_money(agent):
    agent.wealth -= 1

def gain_money(agent):
    agent.wealth += 1

if __name__ == '__main__':
    wealth_distribution = np.random.poisson(50, 10)
    agentset = AgentSet()
    agentset.create(wealth=wealth_distribution)
