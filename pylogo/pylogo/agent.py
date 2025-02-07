"""Agents in the simulation."""
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

    def __init__(self, color=(1,0,0), position=(0,0), size=(1,1)):
        """
        Initializes a new instance of the Agent class.

        Args:
            color (tuple, optional): The color of the agent. Defaults to (1,0,0).
            position (tuple, optional): The position of the agent. Defaults to (0,0).
            size (tuple, optional): The size of the agent. Defaults to (1,1).
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

class AgentSet(AgentBase):
    """
    A class representing a set of agents in an agent-based modeling project.

    Attributes:
        position_dist: The distribution of positions for the agents.
        size_dist: The distribution of sizes for the agents.
        color: The color of the agents.
    """

    def __init__(self, number=100):
        """
        Initializes an AgentSet object.

        Args:
            number (int): The number of agents in the set.
        """
        super().__init__()
        self.position_dist = None
        self.size_dist = None
        self.color = None

    def make_agents(self):
        """
        Creates and returns a list of agents based on the position distribution.

        Returns:
            list: A list of Agent objects.
        """
        return [Agent(position=(x, y)) for x, y in zip(self.position_dist.x_arr, self.position_dist.y_arr)]

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