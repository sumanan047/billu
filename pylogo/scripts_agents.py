from pylogo.agent import Agent
from pylogo.agent import AgentSet


if __name__ == '__main__':

    import numpy as np

    wealth_distribution = np.random.poisson(50, 10)
    age_distribution = np.random.randint(50, 100, 10)
    killing_instinct = np.random.randint(0, 10, 10)
    
    agentset = AgentSet()
    agentset.create(wealth=wealth_distribution, age=age_distribution, kill = killing_instinct)
    

    agentset.remove(agentset.agents[0])
    
    print(len(agentset.agents))