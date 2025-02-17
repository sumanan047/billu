"""Space in simulation"""
import uuid
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
from agent import AgentBase

class Space(AgentBase):
    def __init__(self, x_min=0, x_max=10, y_min=0, y_max=10, color=(1,1,0)):
        # abstract classes don't enforce attributes, this is for documentation only
        self.model = None # name of the model
        self.unique_id = uuid.uuid4() # name of the agent
        self.color = color # color of the
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.sprite = patches.Rectangle((self.x_min, self.y_min),
                                        self.x_max - self.x_min,
                                        self.y_max - self.y_min,
                                        linewidth=1,
                                        edgecolor='black',
                                        facecolor=self.color)
        self.properties = {} # user defined attribs like size, age...

    def register_model(self, model):
        pass

    def register_rule(self, rule):
        pass

    def set_space(self, **kwargs):
        self.properties.update(kwargs)

    def _export(self):
        pass

    def _visualize(self):
        fig, ax = plt.subplots()
        for i in range(100):
            x_min = self.x_min
            x_max = self.x_max
            y_min = self.y_min
            y_max = self.y_max

            x = np.random.uniform(x_min, x_max)
            y = np.random.uniform(y_min, y_max)
            rect = self.sprite.get_bbox()
            rect.x0 = x
            rect.y0 = y
            ax.add_patch(rect)

        ax.set_xlim(self.x_min, self.x_max)
        ax.set_ylim(self.y_min, self.y_max)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Space")
        plt.savefig("space.png")
        plt.show()