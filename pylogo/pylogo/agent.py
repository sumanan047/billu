"""Agents in the simulation."""
from abc import ABC, abstractmethod
import uuid

class AgentBase(ABC):

    @abstractmethod
    def action(self, model):
        """ This is any method that takes in the AgentSet and updates the agent """
        pass

class Agent(AgentBase):
    """
    Represents an agent in the simulation.

    Attributes:
        unique_id (uuid.UUID): The unique identifier of the agent.
        color (tuple): The color of the agent.
        position (tuple): The position of the agent.
        size (tuple): The size of the agent.
    """

    def __init__(self,
                _red = 0,
                _green = 1,
                _blue = 0,
                x_pos = 0,
                y_pos = 0,
                x_size = 1,
                y_size = 1,
                **kwargs):
        """
        Initializes a new instance of the Agent class.

        Args:
            color (tuple, optional): The color of the agent. Defaults to (1,0,0).
            position (tuple, optional): The position of the agent. Defaults to (0,0).
            size (tuple, optional): The size of the agent. Defaults to (1,1).
            **properties: Additional properties of the agent as keyword arguments.
        """
        self.unique_id = str(uuid.uuid4())
        # internally set
        self._red = _red
        self._green = _green
        self._blue = _blue
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._x_size = x_size
        self._y_size = y_size
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        """Optional: Updates the properties of the agent."""
        self.__dict__.update(kwargs)

    def action(self):
        pass

    def __repr__(self) -> str:
        return f'Agent({self.unique_id}, {self._red}, {self._green}, {self._blue}, {self._x_pos}, {self._y_pos}, {self._x_size}, {self._y_size})'


class AgentSet(Agent):

    def __init__(self):
        self.no = 10 # number of agents
        self.agents = [] # list of agents

    def create(self, **dist):
        """
        Create agents based on the given distributions.

        Parameters:
        - dist: A dictionary of distributions, where the keys represent the attributes of the agents and the values are lists of values for each attribute.

        Raises:
        - ValueError: If the length of any distribution list is not equal to the number of agents.

        Returns:
        - None
        """
        for k, v in dist.items():
            if len(v) != self.no:
                raise ValueError(f'Length of {k} should be {self.no}')
        # create agents after asserting the length of the distributions
        for i in range(self.no):
            # create the agent inside the loop
            agent = Agent()
            # update the agent with the values from the distributions
            for k, v in dist.items():
                agent.update(**{k: v[i]})
            self.agents.append(agent)

    def add(self, agent):
        """
        Add an agent to the list of agents.
        
        Parameters:
            agent (object): The agent to be added.
        """
        self.agents.append(agent)

    def remove(self, agent):
        """
        Remove the specified agent from the list of agents.
        
        Args:
            agent: The agent to be removed.
        """
        self.agents.remove(agent)

    def __repr__(self) -> str:
        return f'AgentSet({self.no}, {self.agents})'