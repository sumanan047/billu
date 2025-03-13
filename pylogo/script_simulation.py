from pylogo.agent import TurtleSet
from pylogo.model import Model
from pylogo.simtime import SimTime
from pylogo.simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt

# define the agentsets
money_agent = TurtleSet(numbers = 10)
money_agent.set_prop_constant('money', 50)

# time
time = SimTime(start=0, steps=1, end=1000)

class MoneyModel(Model):
    def __init__(self, time, agent_dict):
        super().__init__(time, agent_dict=money_agent)

    def setup(self):
        self.agent_dict.set_prop_constant('money', 50)

    def step(self, amount = 25):
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
        print("Step is getting called")
        print(f"Winner: {winner_agent.money}")
        print(f"Loser: {loser_agent.money}")

    def save(self):
        print("Saving the model")


# Money model execution
money_model = MoneyModel(time, money_agent)
money_model.setup()
# fig, ax = plt.subplots()
# for i in range(1000):
#     ax.clear
#     money_model.step()
#     print(f"Step: {i}")
#     print(f"Number of Agents: {len(money_agent.turtle_dict)}")
#     print(f"Total Money: {sum([turtle.money for turtle in money_agent.turtle_dict.values()])}")
#     ax.hist([turtle.money for turtle in money_agent.turtle_dict.values()], bins=50)
#     ax.set_xlabel('Money')
#     ax.set_ylabel('Number of Agents')
#     plt.pause(0.1)
# plt.show()

# Simulation
sim = Simulation(model=money_model, time=time)
sim.run()

