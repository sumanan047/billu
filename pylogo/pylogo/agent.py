"""Agents in the simulation."""
from abc import ABC, ABCMeta, abstractmethod
import uuid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from distributions import Distribution_2D, Distribution_1D


class AgentBase(ABC):
    def __init__(self):
        # abstract classes don't enforce attributes, this is for documentation only
        self.model = None # name of the model
        self.unique_id = None # name of the agent
        self.color = None # color of the agent
        self.position = None # tuple in 2D or 3D
        self.size = None # tuple in 2D or 3D
        self.properties = {} # user defined attribs like size, age...
        self.rules = [] # list of rules

    @abstractmethod
    def register_model(self, model):
        """ You can register agents to models. This can help save good agents.
        Load the agents and just register them to a model for reuse."""
        pass

    @abstractmethod
    def register_rule(self, rule):
        """
        You can save rules and load them later and then register them to a model and conduct
        a simulation.
        """
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
    """
    Represents an agent in the simulation.

    Attributes:
        unique_id (uuid.UUID): The unique identifier of the agent.
        color (tuple): The color of the agent.
        position (tuple): The position of the agent.
        size (tuple): The size of the agent.
        sprite (matplotlib.patches.Rectangle): The graphical representation of the agent.
        properties (dict): Additional properties of the agent.
        rules (list): List of rules associated with the agent.
    """

    def __init__(self, color: tuple=(1,0,0),
                position: tuple=(0,0),
                size: tuple=(1,1),
                **kwargs):
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

    def export_agent(self):
        pass

    def visualize(self):
        """
        Visualizes the agent.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.add_patch(self.sprite)
        plt.show()

class AgentSet(AgentBase):
    """
    A class representing a set of agents in an agent-based modeling project.

    Attributes:
        position_dist: The distribution of positions for the agents.
        size_dist: The distribution of sizes for the agents.
        color: The color of the agents.
    """

    def __init__(self, number: int=100,
                position_dist: Distribution_2D=None,
                size_dist: Distribution_2D=None,
                **kwargs):
        """
        Initializes an AgentSet object.

        Args:
            number (int): The number of agents in the set.
        """
        super().__init__()
        self._count = number
        if position_dist is None:
            raise ValueError("position_dist is not set")
        self._position_dist = position_dist
        if size_dist is None:
            raise ValueError("size_dist is not set")
        self._size_dist = size_dist
        self._color = None
        self.agentset_properties = kwargs    # start with keys of the dict filled with unique ids
        self.agents = self._make_agents(self._position_dist, self._size_dist, self._color)

    def __len__(self):
        """Returns the number of agents in the set."""
        return self._count

    def __iter__(self):
        """Returns an iterator over the agents in the set."""
        return iter(self.agents)
    
    def __getitem__(self, key):
        """Returns the agent at the specified index."""
        return self.agents[key]

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

    def _make_agents(self, position_dist: Distribution_2D=None, size_dist: Distribution_2D=None, color: tuple=None):
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
            positions = [(0,0) for _ in range(self._count)]
        if size_dist is not None:
            self._size_dist = size_dist
            sizes = [(x,y) for x, y in zip(self._size_dist.x_arr, self._size_dist.y_arr)]
        else:
            sizes = [(1,1) for _ in range(self._count)]
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
    
    def visualize(self):
        """
        Visualizes the agents in the set.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        for agent in self.agents:
            ax.add_patch(agent.sprite)
        plt.show()


if __name__ == "__main__":

    # create an agent
    a1 = Agent((1,0,0), position= (-3,2), size = (1,1), age=10, gender='male', wealth=100)
    a1.visualize()

    # create an agentset
    d1 = Distribution_2D()
    d1.uniform(low=[-15,0], high=[1,7], size=100)
    d2 = Distribution_2D()
    d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=100)
    d3 = Distribution_1D()
    d3.normal(mean=33, std=10, size=100)

    # unwrap d1.x_arr and d1.y_arr to fill AgentSet positions
    ag1 = AgentSet(number = 100, position_dist=d1, size_dist=d2,age=d3)
    ag1.visualize()
