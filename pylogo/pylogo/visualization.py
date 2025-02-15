import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Canvas:
    def __init__(self, width, height, agents = []):
        self.width = width
        self.height = height
        self.mode = None
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def update(self):
        for agent in self.agents:
            agent.update()

    def viz(self):
        pass

if __name__ == "__main__":
    # create an agentset
    from distributions import Distribution_2D
    from agent import AgentSet

    d1 = Distribution_2D()
    d1.uniform(low=[0,1], high=[10,7], size=100)

    d2 = Distribution_2D()
    d2.uniform(low=[0.1,0.1], high=[0.1,0.1], size=100)

    ag1 = AgentSet(number = 100, position_dist=d1, size_dist=d2)

    canvas = Canvas(100, 100, agents=ag1.agents)
    canvas.viz()