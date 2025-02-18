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
        self.current_time = start_time # start with the start_time and then change

    def __iter__(self):
        self.current_time = self.start_time
        return self

    def __next__(self):
        if self.current_time + self.time_step < self.end_time:
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
        if len(list(sim_agent_rules.keys())) == 0:
            raise ValueError("The simulation agent rules dictionary cannot be empty.")
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
