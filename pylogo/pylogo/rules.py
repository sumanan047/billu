"""This modules contains the rules for the pylogo.
Some rules are provided and others can be developed by the user
based on the rules template from this module."""
from .agent import Agent, AgentSet
import numpy as np
from typing import Union

# a collection of simple rules for agents
def move_to(bound_agent: Union[Agent, AgentSet], x, y):
    """
    Move the bound_agent to the specified coordinates (x, y).

    Parameters:
    bound_agent (Agent or AgentSet): The agent or agent set to be moved.
    x (int or float): The x-coordinate to move the agent to.
    y (int or float): The y-coordinate to move the agent to.

    Raises:
    ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_to(ag, x, y)
    else:
        bound_agent.x_pos = x
        bound_agent.y_pos = y
        # update the dicts
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_by(bound_agent: Union[Agent, AgentSet], dx = 1, dy = 1):
    """
    Move the given agent or agents by the specified amount in the x and y directions.

    Parameters:
    bound_agent (Agent or AgentSet): The agent or agent set to be moved.
    dx (int): The amount to move in the x direction. Default is 1.
    dy (int): The amount to move in the y direction. Default is 1.

    Raises:
    ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_by(ag, dx, dy)
    else:
        bound_agent.x_pos += dx
        bound_agent.y_pos += dy
        # update the dicts
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_up(bound_agent: Union[Agent, AgentSet], distance=1):
    """
    Moves the given agent or agents in the upward direction by the specified distance.
    
    Parameters:
        bound_agent (Agent or AgentSet): The agent or agents to be moved.
        distance (int, optional): The distance to move the agent(s) upward. Default is 1.
    
    Raises:
        ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_up(ag, distance)
    else:
        bound_agent.y_pos += distance
        # update the dicts
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_down(bound_agent: Union[Agent, AgentSet], distance=1):
    """
    Move the bound_agent down by the specified distance.

    Parameters:
    bound_agent (Agent or AgentSet): The agent or agent set to be moved.
    distance (int, optional): The distance to move the agent down. Default is 1.

    Raises:
    ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """

    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_down(ag, distance)
    else:
        bound_agent.y_pos -= distance
        # update the dicts
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_left(bound_agent: Union[Agent, AgentSet], distance=1):
    """
    Move the bound_agent to the left by the specified distance.

    Parameters:
    bound_agent (Agent or AgentSet): The agent or agent set to be moved.
    distance (int): The distance to move the agent(s). Default is 1.

    Raises:
    ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """

    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_left(ag, distance)
    else:
        bound_agent.x_pos -= distance
        # update the dicts
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos

def move_right(bound_agent: Union[Agent, AgentSet], distance=1):
    """
    Moves the bound_agent to the right by the specified distance.
    
    Parameters:
        bound_agent (Agent or AgentSet): The agent or agent set to be moved.
        distance (int, optional): The distance to move the agent(s) to the right. Default is 1.
    
    Raises:
        ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.
    """
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_right(ag, distance)
    else:
        bound_agent.x_pos += distance
        # update the dicts
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos

def move_by_at_angle(bound_agent: Union[Agent, AgentSet], distance, angle):
    """
    Moves the bound_agent by a given distance at a given angle.

    Parameters:
    bound_agent (Agent or AgentSet): The agent or agent set to be moved.
    distance (float): The distance to move the agent(s).
    angle (float): The angle in radians at which to move the agent(s).

    Raises:
    ValueError: If the bound_agent is not an instance of the Agent or AgentSet class.

    """
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_by_at_angle(ag, distance, angle)
    else:
        bound_agent.x_pos += distance * np.cos(angle)
        bound_agent.y_pos += distance * np.sin(angle)
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

