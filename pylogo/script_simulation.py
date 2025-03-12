import numpy as np
from pylogo.simtime import SimTime
from pylogo.agent import AgentSet
import matplotlib.pyplot as plt

NO_AGENTS = 100

# Define time
_time = SimTime(0, 1, 1000).arr

# Define agentset
wealth_distribution = np.random.uniform(500,500,NO_AGENTS)
agentset = AgentSet(no=NO_AGENTS)
agentset.create(wealth=wealth_distribution)



fig, ax = plt.subplots()

# Define simulation
for t in _time:
    ax.clear()
    # print(f'Time: {t}')
    # print(np.random.choice(agentset.agents))
    ag1, ag2 = np.random.choice(agentset.agents, 2)

    # @ag1.action
    def loose_money(agent):
        if agent.wealth > 100:
            agent.wealth -= 100

    # @ag2.action
    def gain_money(agent):
        if agent.wealth < 100:
            agent.wealth += 100

    loose_money(ag1)
    gain_money(ag2)

    ax.hist([agent.wealth for agent in agentset.agents], bins=50, color='green', alpha=0.7, edgecolor='black')
    ax.set_ylim(0, NO_AGENTS)  # Set y-axis limits
    plt.pause(0.01)  # Reduce the pause duration for faster animation
plt.show()