"""Agents in the simulation."""
from abc import ABC, abstractmethod
import uuid
import types
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .distributions import Distribution_2D, Distribution_1D
import pandas as pd


class AgentBase(ABC):
    def __init__(self):
        # abstract classes don't enforce attributes, this is for documentation only
        self.model = None # name of the model
        self.unique_id = None # name of the agent
        self.color = None # color of the agent
        self.position = None # tuple in 2D or 3D
        self.size = None # tuple in 2D or 3D
        self.properties = {} # user defined attribs like size, age...

    @abstractmethod
    def register_model(self, model):
        """ You can register agents to models. This can help save good agents.
        Load the agents and just register them to a model for reuse."""
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
        self.unique_id = str(uuid.uuid4())
        # properties to be set by the user
        self.color = color
        # internally set
        self._r_color = self.color[0]
        self._g_color = self.color[1]
        self._b_color = self.color[2]
        # properties to be set by the user
        self.position = position
        # internally set
        self.x_pos = self.position[0]
        self.y_pos = self.position[1]
        # properties to be set by the user
        self.size = size
        # internally set
        self.x_size = self.size[0]
        self.y_size = self.size[1]
        # create the sprite for visualization in matplotlib
        self.sprite = patches.Rectangle(self.position,
                                        self.size[0],
                                        self.size[1],
                                        linewidth=1,
                                        edgecolor='black',
                                        facecolor=self.color)
        # properties to be set by the user
        self.properties = kwargs
        # dict form of agent
        self.agent_dict = { "unique_id": [self.unique_id],
                            "r_color": [self._r_color],
                            "g_color": [self._g_color],
                            "b_color": [self._b_color],
                            "x_pos": [self.x_pos],
                            "y_pos": [self.y_pos],
                            "x_size": [self.x_size],
                            "y_size": [self.y_size]}
        self.agent_dict.update(self.properties)

    def register_model(self, model):
        """
        Registers the agent with the given model.

        Args:
            model (Model): The model to register the agent with.
        """
        super().register_model(model)
        pass

    def register_rule(self, method_name, func):
        """
        Adds a dynamic method to the class instance that can use class attributes.

        Args:
          method_name: The name of the method to be added.
          func: The function to be used as the method.
        """
        def dynamic_method_wrapper(self, *args, **kwargs):
                # Access class attributes here
                result = func(self, *args, **kwargs)  # Call the original function
                return result
        setattr(self, method_name, types.MethodType(dynamic_method_wrapper, self))

    def set_properties(self, **kwargs):
        """
        Sets the properties of the agent.

        Args:
            **kwargs: The properties to set.
        """
        self.properties.update(kwargs)

    def _visualize(self):
        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        sprite = patches.Rectangle((self.x_pos, self.y_pos), self.x_size, self.y_size)  # Create a new instance
        ax.add_patch(sprite)
        plt.show()

    def _export(self):
        """
        Exports the agent to a dictionary.

        Returns:
            dict: A dictionary representation of the agent.
        """
        pd.DataFrame(self.agent_dict).to_csv(f"agent_{self.unique_id}.csv")
        return pd.DataFrame(self.agent_dict)

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
                color = (1,0,0),
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
        # assrtion to check if both items in the tuple of Distribution 2D
        # are of length equal to self._count
        if len(position_dist.x_arr) != self._count or len(position_dist.y_arr) != self._count:
            raise ValueError("position_dist must have the same length as the number of agents")
        self._position_dist = position_dist
        if size_dist is None:
            raise ValueError("size_dist is not set")
        # check if both items in the tuple of Distribution 2D are of length equal to self._count
        if len(size_dist.x_arr) != self._count or len(size_dist.y_arr) != self._count:
            raise ValueError("size_dist must have the same length as the number of agents")
        self._size_dist = size_dist
        self._color = color
        if not all(isinstance(value, Distribution_1D) for value in kwargs.values()):
            raise TypeError("kwargs must contain Distribution1D objects")
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
        if len(self.agentset_properties.keys()) == 0:
            return agents
        else:
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
    
    def _visualize(self):
        """
        Visualizes the agents in the set.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        for agent in self.agents:
            ax.add_patch(agent.sprite)
        plt.show()

    def _export(self, filename: str="agentset.csv"):
            """
            Exports the agents in the set to a dictionary and saves it as a CSV file
            and return a dataframe.

            Returns:
                pandas.DataFrame: A DataFrame representation of the agents in the set.
            """
            # creates a list of dicts for each agent
            agentset_dicts = [{k: v[0] for k, v in agent.agent_dict.items()} for agent in self.agents]
            # make a dataframe from the list of dicts
            pd.DataFrame(agentset_dicts).to_csv(filename)
            return pd.DataFrame(agentset_dicts)