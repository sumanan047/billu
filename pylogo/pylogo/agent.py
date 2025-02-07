from abc import ABC, ABCMeta, abstractmethod
import uuid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class AgentBase(ABC):
    def __init__(self):
        self.model = None
        self.unique_id = None
        self.color = None
        self.position = None # tuple
        self.size = None # tuple
        self.attributes = {} # user defined attribs like size, age...
        self.rules = []

    @abstractmethod
    def register_model(self, model):
        pass

    @abstractmethod
    def register_rule(self, rule):
        pass

class TupleDescriptor:
    def __get__(self, instance, owner):
        return instance._tuple

    def __set__(self, instance, value):
        if isinstance(value, tuple) and all(0 <= item <= 1 for item in value):
            instance._tuple = value
        else:
            raise ValueError("Tuple elements must be between 0 and 1")

class Agent(AgentBase):
    def __init__(self, color=(1,0,0), position = (0,0), size = (1,1)):
        super().__init__()
        self.unique_id = uuid.uuid4()
        self.color = color
        self.position = position
        self.size = size
        self.sprite = patches.Rectangle(self.position,
                                        self.size[0],
                                        self.size[1],
                                        linewidth=1,
                                        edgecolor='black',
                                        facecolor=self.color)

    def register_model(self, model):
        super().register_model(model)
        pass

    def register_rule(self, rule):
        super().register_rule(rule)
        pass

class AgentSet(AgentBase):
    def __init__(self, number = 100):
        super().__init__()
        self.position_dist = None
        self.size_dist = None
        self.color = None

    def make_agents(self):
        return [Agent(position=(x,y)) for x,y in zip(self.position_dist.x_arr, self.position_dist.y_arr)]

    def register_model(self, model):
        return super().register_model(model)
        pass

    def register_rule(self, rule):
        return super().register_rule(rule)
        pass


if __name__ == "__main__":
    from distributions import Distribution
    
    a1 = Agent((1,0,0), position= (-3,2), size = (1,1))
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.add_patch(a1.sprite)
    plt.show()

    # create an agentset
    d1 = Distribution()
    d1.uniform(low=[-10,0], high=[3,5], size=100)
    # unwrap d1.x_arr and d1.y_arr to fill AgentSet positions
    ag1 = AgentSet(number = 100)
    ag1.position_dist = d1
    ag1.make_agents()

    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    for age in ag1.make_agents():
        ax.add_patch(age.sprite)
    plt.show()