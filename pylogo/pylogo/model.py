"""To be made useful in future version. Right now it is just a dummy class"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from agent import AgentSet
from space import Space
import numpy as np

class Model:
    def __init__(self, agentset, space) -> None:
        self.model_id = None
        self.agentset = agentset
        self.space = space

    def setup(self):
        pass

    def visualize(self):
        fig, ax = plt.subplots()
        ax.set_xlim(self.space.x_min, self.space.x_max)
        ax.set_ylim(self.space.y_min, self.space.y_max)
        for agent in self.agentset:
            rect = agent.sprite
            ax.add_patch(rect)
        for i in range(100):
            x_min = 0.0
            x_max = 10.0
            y_min = 0.0
            y_max = 10.0

            x = np.random.uniform(x_min, x_max)
            y = np.random.uniform(y_min, y_max)
            rect = Rectangle((x, y), self.space.size, self.space.size, facecolor=self.space.color)
            ax.add_patch(rect)
        plt.show()

    def step(self):
        pass



if __name__ == "__main__":
    # Create an agentset and space
    from distributions import Distribution_2D, Distribution_1D
    d1 = Distribution_2D()
    d1.uniform(low=[0,1], high=[10,7], size=100)
    d11 = Distribution_2D()
    d11.uniform(low=[0,1], high=[10,7], size=100)
    d2 = Distribution_2D()
    d2.uniform(low=[0.1,0.1], high=[0.1,0.1], size=100)
    d3 = Distribution_1D()
    d3.normal(mean=33, std=10, size=100)

    # create agents
    ag1 = AgentSet(number = 100, age=d3)
    ag_list = ag1._make_agents(position_dist=d1, size_dist=d2, color=(1,0,0))


    # another agent
    ag2 = AgentSet(number = 100, age=d3)
    ag_list2 = ag2._make_agents(position_dist=d11, size_dist=d2, color=(0,1,0))

    # create space
    sp = Space(x_min=0, x_max=10, y_min=0, y_max=10, size=1, color=(1,1,0))
    
    ag_list.extend(ag_list2)

    # create model
    m = Model(ag_list,sp)
    m.setup()
    m.visualize()