from pylogo.agent import TurtleSet
from pylogo.model import Model
from pylogo.simtime import SimTime
from pylogo.simulation import Simulation


NO_SHEEP = 10
NO_WOLVES = 5
TIME_STEP = 1
END_TIME = 100
NO_FRAMES = 100

# define the agentsets
sheep_agent = TurtleSet(numbers = NO_SHEEP)
wolf_agent = TurtleSet(numbers = NO_WOLVES)

# time
time = SimTime(start=0, steps=TIME_STEP, end=END_TIME)

class PredatorPrey(Model):
    def __init__(self, time, agent_dict, **kwargs):
        super().__init__(time, agent_dict, **kwargs)
    
    def setup(self):
        print("Setting up the model")
        print("self.agent_dict", self.agent_dict)
        self.agent_dict['wolf_agent'].set_prop_constant('energy', 10)
        self.agent_dict['wolf_agent'].set_prop_constant('hunger', 0)

    def step(self):
        print("Stepping the model")
        print("self.agent_dict", self.agent_dict)


pp = PredatorPrey(time,
                agent_dict={'sheep_agent': sheep_agent, 'wolf_agent': wolf_agent})
pp.setup()
