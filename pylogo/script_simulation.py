from pylogo.agent import TurtleSet
from pylogo.model import Model
from pylogo.simtime import SimTime
import numpy as np
import matplotlib.pyplot as plt

# define the agentsets
money_agent = TurtleSet(numbers = 1000)
money_agent.set_prop_constant('money', 50)

# time
time = SimTime(start=0, steps=1, end=1000)

class MoneyModel(Model):
    def __init__(self, time, agent_dict):
        super().__init__(time, agent_dict=money_agent)

    def setup(self):
        self.agent_dict.set_prop_constant('money', 50)

    def step(self):
        EXCHANGE_AMOUNT = 25
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

        plt.hist([_agent.__dict__['money'] for _agent in self.agent_dict.turtle_dict.values()], bins=int(2*np.log(self.agent_dict.numbers)))
        # money agent
    def save(self):
        pass


# Money model execution
money_model = MoneyModel(time, money_agent)
money_model.setup()
# make below an animation
fig, ax = plt.subplots()
for t in time:
    ax.clear()
    money_model.step()
    plt.pause(0.1)
    # save is a fake method for now
    money_model.save()
# plt.hist([_agent.__dict__['money'] for _agent in money_agent.turtle_dict.values()], bins=int(2*np.log(money_agent.numbers)))