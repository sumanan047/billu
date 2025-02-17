"""This is the main simulation module for the pylogo package."""
from agent import Agent
from rules import move_by_at_angle

class simulation:
    def __init__(self, sim_agent:Agent, rule:callable):
        self.sim_agent = sim_agent
        self.rule = rule

    def run_simulation(self):
        pass


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    # make an agent
    ag = Agent()
    # make a rule
    ag.register_rule('move_by_at_angle', move_by_at_angle)
    # make a simulation
    sim = simulation(ag, move_by_at_angle)
    # run the simulation
    fig , ax = plt.subplots()
    low_limit = -100
    high_limit = 100
    ax.set_xlim(low_limit, high_limit)
    ax.set_ylim(low_limit, high_limit)
    ax.set_aspect('equal')
    ag_dict_list = []
    for i in range(10):
        ag.move_by_at_angle(10, np.pi/2)
        ag_dict_list.append(ag.agent_dict)
        ax.clear()
        ax.set_xlim(low_limit, high_limit)
        ax.set_ylim(low_limit, high_limit)
        ax.set_aspect('equal')
        ax.plot(ag.x_pos, ag.y_pos, 'ro')
        plt.pause(0.1)
    plt.show()
    import pandas as pd
    df = pd.DataFrame(ag_dict_list)
    print(df)
