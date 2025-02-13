"""Space in simulation"""
import uuid
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from agent import AgentBase


class Space(AgentBase):
    def __init__(self, x_min=0, x_max=10, y_min=0, y_max=10, size=1, color=(1,1,0)):
        # abstract classes don't enforce attributes, this is for documentation only
        self.model = None # name of the model
        self.unique_id = uuid.uuid4() # name of the agent
        self.color = color # color of the
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.size = size
        self.properties = {} # user defined attribs like size, age...
        self.rules = [] # list of rules

    def register_model(self, model):
        pass

    def register_rule(self, rule):
        pass

    def set_space(self, **kwargs):
        self.properties.update(kwargs)

    def export(self):
        pass

    def visualize(self):
        fig, ax = plt.subplots()
        for i in range(100):
            x_min = 0.0
            x_max = 10.0
            y_min = 0.0
            y_max = 10.0

            x = np.random.uniform(x_min, x_max)
            y = np.random.uniform(y_min, y_max)
            rect = Rectangle((x, y), self.size, self.size, facecolor=self.color)
            ax.add_patch(rect)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Space")
        plt.savefig("space.png")
        plt.show()

if __name__ == "__main__":
    sp = Space(x_min=0, x_max=10, y_min=0, y_max=10, size=1, color=(1,1,0))
    sp.set_space()
    sp.visualize()
    print(sp.properties)
    print(sp.unique_id)