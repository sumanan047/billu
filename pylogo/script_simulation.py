from pylogo.agent import TurtleSet
from pylogo.model import Model
from pylogo.simtime import SimTime
from pylogo.simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt

NO_OF_AGENTS = 10
TOTAL_MONEY = 500 # 50$ to each agent
MONEY_PER_AGENT = 50
EXCHANGE_AMOUNT = 25
TIME_STEP = 1
END_TIME = 100
NO_FRAMES = 100

# define the agentsets
money_agent = TurtleSet(numbers = NO_OF_AGENTS)
money_agent.set_prop_constant('money', MONEY_PER_AGENT)

# time
time = SimTime(start=0, steps=TIME_STEP, end=END_TIME)

class MoneyModel(Model):
    def __init__(self, time, agent_dict):
        super().__init__(time, agent_dict=money_agent)

    def setup(self):
        self.agent_dict.set_prop_constant('money', MONEY_PER_AGENT)

    def step(self, amount = EXCHANGE_AMOUNT):
        EXCHANGE_AMOUNT = amount
        # loser_agent with money more than 10
        filtered_agent = self.agent_dict.filter_agents_greater_than('money', EXCHANGE_AMOUNT)
        # choose from the filtered agents
        loser_agent = np.random.choice(filtered_agent)
        # winner agent
        winner_agent = np.random.choice(list(self.agent_dict.turtle_dict.values()))
        while winner_agent.id == loser_agent.id:
            winner_agent = np.random.choice(list(self.agent_dict.turtle_dict.values()))
        loser_agent.inc_prop('money', -EXCHANGE_AMOUNT)
        winner_agent.inc_prop('money', EXCHANGE_AMOUNT)

    def save(self):
        print("Saving the model")


# Money model execution
money_model = MoneyModel(time, money_agent)
money_model.setup()

# Simulation
sim = Simulation(model=money_model, time=time)
sim.run(property_name='money',
        type='histogram',
        plot_dict={'xlabel': 'Money', 'ylabel': 'Number of Agents', 'title': 'Money Distribution', 'xlim': (0, MONEY_PER_AGENT*10), 'ylim': (0, NO_OF_AGENTS*2)},
        animation_dict={'frames': NO_FRAMES, 'interval': NO_FRAMES})

