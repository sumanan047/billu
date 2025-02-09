"""Agents in the simulation."""
from abc import ABC, ABCMeta, abstractmethod
import uuid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from distributions import Distribution_2D, Distribution_1D


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

import uuid
import matplotlib.patches as patches

class Agent(AgentBase):
    """
    Represents an agent in the simulation.

    Attributes:
        unique_id (uuid.UUID): The unique identifier of the agent.
        color (tuple): The color of the agent.
        position (tuple): The position of the agent.
        size (tuple): The size of the agent.
        sprite (matplotlib.patches.Rectangle): The graphical representation of the agent.
    """

    def __init__(self, color=(1,0,0), position=(0,0), size=(1,1), **kwargs):
        """
        Initializes a new instance of the Agent class.

        Args:
            color (tuple, optional): The color of the agent. Defaults to (1,0,0).
            position (tuple, optional): The position of the agent. Defaults to (0,0).
            size (tuple, optional): The size of the agent. Defaults to (1,1).
            **properties: Additional properties of the agent as keyword arguments.
        """
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
        self.properties = kwargs

    def register_model(self, model):
        """
        Registers the agent with the given model.

        Args:
            model (Model): The model to register the agent with.
        """
        super().register_model(model)
        pass

    def register_rule(self, rule):
        """
        Registers the rule with the agent.

        Args:
            rule (Rule): The rule to register with the agent.
        """
        super().register_rule(rule)
        pass

    def set_properties(self, **kwargs):
        """
        Sets the properties of the agent.

        Args:
            **kwargs: The properties to set.
        """
        self.properties.update(kwargs)

class AgentSet(AgentBase):
    """
    A class representing a set of agents in an agent-based modeling project.

    Attributes:
        position_dist: The distribution of positions for the agents.
        size_dist: The distribution of sizes for the agents.
        color: The color of the agents.
    """

    def __init__(self, number=100, **kwargs):
        """
        Initializes an AgentSet object.

        Args:
            number (int): The number of agents in the set.
        """
        super().__init__()
        self.count = number
        self._position_dist = None
        self._size_dist = None
        self._color = None
        self.agentset_properties = kwargs    # start with keys of the dict filled with unique ids

    @property
    def position_dist(self):
        if self._position_dist is None:
            raise ValueError("position_dist is not set")
        else:
            return self._position_dist

    @position_dist.setter
    def position_dist(self, value):
        if isinstance(value, Distribution_2D):
            self._position_dist = value
        else:
            raise TypeError("position_dist must be a Distribution object")

    def make_agents(self, position_dist: Distribution_2D=None, size_dist: Distribution_2D=None, color: tuple=None):
        """
        Creates and returns a list of agents based on the position distribution.

        Returns:
            list: A list of Agent objects.
        """
        # is user wants to override the distribution it can be set here
        positions = []
        sizes = []
        if position_dist is not None:
            self.position_dist = position_dist
            positions = [(x,y) for x, y in zip(self.position_dist.x_arr, self.position_dist.y_arr)]
        else:
            positions = [(0,0) for _ in range(self.count)]
        if size_dist is not None:
            self._size_dist = size_dist
            sizes = [(x,y) for x, y in zip(self._size_dist.x_arr, self._size_dist.y_arr)]
        else:
            sizes = [(1,1) for _ in range(self.count)]
        if color is not None:
            self._color = color
        agents = [Agent(color=self._color, position=pos, size=size) for pos, size in zip(positions, sizes)]
        # go thorugh the property set and set for each agent
        for key, value in self.agentset_properties.items():
            for i, agent in enumerate(agents):
                agent.properties[key] = value[i]
        return agents

    def register_model(self, model):
        """
        Registers the model with the AgentSet.

        Args:
            model: The model to be registered.

        Returns:
            The registered model.
        """
        return super().register_model(model)

    def register_rule(self, rule):
        """
        Registers a rule with the AgentSet.

        Args:
            rule: The rule to be registered.

        Returns:
            The registered rule.
        """
        return super().register_rule(rule)


if __name__ == "__main__":

    # create an agent
    a1 = Agent((1,0,0), position= (-3,2), size = (1,1), age=10, gender='male', wealth=100)
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.add_patch(a1.sprite)
    plt.show()
    print(a1.unique_id, a1.color, a1.position, a1.size, a1.properties)

    # create an agentset
    d1 = Distribution_2D()
    d1.uniform(low=[-15,0], high=[1,7], size=100)
    d2 = Distribution_2D()
    d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=100)
    d3 = Distribution_1D()
    d3.normal(mean=33, std=10, size=100)

    # unwrap d1.x_arr and d1.y_arr to fill AgentSet positions
    ag1 = AgentSet(number = 100, age=d3)
    ag_list = ag1.make_agents(position_dist=d1, size_dist=d2, color=(1,0,0))

    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    for age in ag_list:
        ax.add_patch(age.sprite)
    plt.show()
    print(ag1.agentset_properties['age'])
    plt.hist(ag1.agentset_properties['age'].data)
    plt.show()
    print(ag_list[1].properties)
