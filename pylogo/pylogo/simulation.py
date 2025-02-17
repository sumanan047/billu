"""This is the main simulation module for the pylogo package."""
import numpy as np
import pandas as pd
from .agent import Agent
from .rules import move_by_at_angle, move_up, move_down, move_left, move_right


class Time:
    def __init__(self, start_time, end_time, time_step):
        self.start_time = start_time
        self.end_time = end_time
        self.time_step = time_step

    def __iter__(self):
        self.current_time = self.start_time
        return self

    def __next__(self):
        if self.current_time < self.end_time:
            self.current_time += self.time_step
            return self.current_time
        else:
            raise StopIteration
    
    def __str__(self):
        return f"Time object with start_time: {self.start_time}, end_time: {self.end_time}, time_step: {self.time_step}"
    
    def time_array(self):
        return np.arange(self.start_time, self.end_time, self.time_step)


class simulation:
    def __init__(self, sim_agent_rules: dict, _time: Time = None):
        self.sim_agent_rules = sim_agent_rules
        self._time = _time
        self.data = None # dataframe to store the simulation data
        for key, value in sim_agent_rules.items():
            if isinstance(key, Agent) and all(callable(func) for func in value):
                for v in value:
                    key.register_rule(str(v.__name__), v)
            else:
                raise ValueError("rules_list must contain only callable objects.")

    def run_simulation(self,
                       export = True,
                       filename = "simulation.csv", *args, **kwargs):
        """
        User should ovveride this method to run the simulation.
        """
        # bind all the values in the self.sim_agent_rules to the key in the dictionary
        # and then call the function with the arguments and keyword arguments
        time_step_list_for_dicts = []
        for _t in self._time:
            for key, value in self.sim_agent_rules.items():
                # keys are the agents and values are the functions to be called
                for v in value:
                    # iterate through all the functions in the value list
                    # Get the parameters of the function
                    params = v.__code__.co_varnames[:v.__code__.co_argcount]
                    # Filter the arguments and keyword arguments based on the function parameters
                    filtered_args = [arg for arg in args if arg in params]
                    filtered_kwargs = {k: v for k, v in kwargs.items() if k in params}
                    # Call the function with the filtered arguments and keyword arguments
                    key.__dict__[v.__name__](*filtered_args, **filtered_kwargs)
            key.agent_dict['time'] = _t
            time_step_list_for_dicts.append(key.agent_dict.copy())
            # print(f"Agent: {key.agent_dict}")
            # make a dataframe from the list of dictionaries
            self.data = pd.DataFrame(time_step_list_for_dicts)
            if export:
                self.data = self.data.apply(lambda x: x.apply(lambda y: y[0] if isinstance(y, list) else y))
                self.data.to_csv(filename)


    def save_simulation(self):
        """
        User should ovveride this method to save the simulation.
        """
        print("Simulation saved.")


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    # make an agent
    ag = Agent()
    _t = Time(0, 10, 0.1)
    # make a simulation
    sim = simulation({ag: [move_by_at_angle, move_up]}, _t)
    sim.run_simulation(distance=1, angle=np.pi/10)
    sim.save_simulation()
    # working .... simulation
    # run the simulation
    # fig , ax = plt.subplots()
    # low_limit = -100
    # high_limit = 100
    # ax.set_xlim(low_limit, high_limit)
    # ax.set_ylim(low_limit, high_limit)
    # ax.set_aspect('equal')
    # ag_dict_list = []
    # x = []
    # y = []
    # for i in range(10):
    #     ag.move_by_at_angle(i*0.5, i*np.pi/10)
    #     ag_dict_list.append(ag.agent_dict.copy())
    #     ax.clear()
    #     ax.set_xlim(low_limit, high_limit)
    #     ax.set_ylim(low_limit, high_limit)
    #     ax.set_aspect('equal')
    #     x.append(ag.x_pos)
    #     y.append(ag.y_pos)
    #     ax.plot(x, y, 'r-')
    #     plt.pause(0.1)
    # plt.show()
    # import pandas as pd
    # df = pd.DataFrame(ag_dict_list)
    # df = df.apply(lambda x: x.apply(lambda y: y[0] if isinstance(y, list) else y))
    # print(df)
