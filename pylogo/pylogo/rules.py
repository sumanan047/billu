"""This modules contains the rules for the pylogo.
Some rules are provided and others can be developed by the user
based on the rules template from this module."""
from .agent import Agent, AgentSet
import numpy as np
from typing import Union

# a collection of simple rules for agents
def move_to(bound_agent, x, y):
    bound_agent.x_pos = x
    bound_agent.y_pos = y
    # update the dicts
    bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
    bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_by(bound_agent, dx = 1, dy = 1):
    bound_agent.x_pos += dx
    bound_agent.y_pos += dy
    # update the dicts
    bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
    bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_up(bound_agent, distance=1):
    # print("Moving up")
    bound_agent.y_pos += distance
    # update the dicts
    bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_down(bound_agent, distance=1):
    bound_agent.y_pos -= distance
    # update the dicts
    bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

def move_left(bound_agent, distance=1):
    bound_agent.x_pos -= distance
    # update the dicts
    bound_agent.agent_dict['x_pos'] = bound_agent.x_pos

def move_right(bound_agent, distance=1):
    bound_agent.x_pos += distance
    # update the dicts
    bound_agent.agent_dict['x_pos'] = bound_agent.x_pos

def move_by_at_angle(bound_agent: Union[Agent, AgentSet], distance, angle):
    if not isinstance(bound_agent, (Agent, AgentSet)):
        raise ValueError("The bound_agent must be an instance of the Agent or AgentSet class.")
    elif isinstance(bound_agent, AgentSet):
        for ag in bound_agent.agents:
            move_by_at_angle(ag, distance, angle)
    else:
        # print(f"Moving by {distance} at angle {angle}")
        bound_agent.x_pos += distance * np.cos(angle)
        bound_agent.y_pos += distance * np.sin(angle)
        # update the dicts
        bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
        bound_agent.agent_dict['y_pos'] = bound_agent.y_pos

# a collection of simple rules for agentsets