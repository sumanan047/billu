from pylogo.pylogo.agent import Agent, AgentSet
from pylogo.pylogo.distributions import Distribution_2D, Distribution_1D
import matplotlib.pyplot as plt


# create distributions
d1 = Distribution_2D()
d1.uniform(low=[-15,0], high=[1,7], size=100)
d2 = Distribution_2D()
d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=100)
d3 = Distribution_1D()
d3.normal(mean=33, std=10, size=100)

# unwrap d1.x_arr and d1.y_arr to fill AgentSet positions
ag1 = AgentSet(number = 100, age=d3)
ag_list = ag1.make_agents(position_dist=d1, size_dist=d2, color=(1,0,0))

# visualize the agents
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
for age in ag_list:
    ax.add_patch(age.sprite)
plt.show()
plt.hist(ag1.agentset_properties['age'].data)
plt.show()