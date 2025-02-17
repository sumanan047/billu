"""This modules contains the rules for the PyLogo language.
Some rules are provided and others can be developed by the user
based on the rules template from this module."""

from abc import ABC, abstractmethod
from agent import Agent, AgentSet
import numpy as np

class RuleBase(ABC):

    @abstractmethod
    def apply(self):
        pass



class Rule(RuleBase):
    def __init__(self, agent, preconditions=None, action=None):
        self.agent = agent
        self.preconditions = preconditions
        self.action = action
        agent.rules.append(self.action)

    def apply(self):
        self.action()


# a collection of simple rules
def move_to(bound_agent, x, y):
    bound_agent.x_pos = x
    bound_agent.agent.y_pos = y

def move_by(bound_agent, dx = 1, dy = 1):
    bound_agent.x_pos += dx
    bound_agent.y_pos += dy

def move_up(bound_agent):
    bound_agent.y_pos += 1

def move_down(bound_agent):
    bound_agent.y_pos -= 1

def move_left(bound_agent):
    bound_agent.x_pos -= 1

def move_right(bound_agent):
    bound_agent.x_pos += 1

def move_by_at_angle(bound_agent, distance, angle):
    bound_agent.x_pos += distance * np.cos(angle)
    bound_agent.y_pos += distance * np.sin(angle)
    # print(f'x_pos: {bound_agent.x_pos}, y_pos: {bound_agent.y_pos}')
    # bound_agent.position = (bound_agent.x_pos, bound_agent.y_pos)
    # print(f'position: {bound_agent.position}')
    # update the agent's dictionary agent_dict with the new position
    bound_agent.agent_dict['x_pos'] = bound_agent.x_pos
    bound_agent.agent_dict['y_pos'] = bound_agent.y_pos


if __name__ == '__main__':
    # define an agent
    ag = Agent()
    # define a rule
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    low_limit = -100
    high_limit = 100
    ax.set_xlim(low_limit, high_limit)
    ax.set_ylim(low_limit, high_limit)
    ax.set_aspect('equal')

    # Initialize lists to store positions
    x_positions = [ag.x_pos]
    y_positions = [ag.y_pos]

    for i in range(100):
        # get a random distance and angle
        rand_dist = np.random.uniform(0, 1, 1)
        rand_angle = np.random.uniform(0, np.pi, 1)
        move_by_at_angle(ag, i, i*np.pi/3)
        
        # Append current position to lists
        x_positions.append(ag.x_pos)
        y_positions.append(ag.y_pos)
        
        # Clear the previous plot
        ax.clear()
        ax.set_xlim(low_limit, high_limit)
        ax.set_ylim(low_limit, high_limit)
        ax.set_aspect('equal')
        
        # Plot the positions
        ax.plot(x_positions, y_positions, 'k')
        plt.pause(0.1)
    plt.show()


