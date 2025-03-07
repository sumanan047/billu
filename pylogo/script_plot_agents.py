import matplotlib.pyplot as plt
from pylogo import agent, distributions

# Agent Numbers
NO_WOLVES = 50
NO_SHEEP = 100

# write distributions
d1 = distributions.Distribution_2D()
d1.uniform(low=[0,1], high=[10,7], size=NO_SHEEP)
d2 = distributions.Distribution_2D()
d2.uniform(low=[0.1,0.1], high=[0.1,0.1], size=NO_SHEEP)
d3 = distributions.Distribution_2D()
d3.uniform(low=[2,2], high=[8,8], size=NO_WOLVES)
d4 = distributions.Distribution_2D()
d4.uniform(low=[0.1,0.1], high=[0.1,0.1], size=NO_WOLVES)

# create agents
sheeps = agent.AgentSet(number = NO_SHEEP, position_dist=d1, size_dist=d2, color=(0,1,0))
wolves = agent.AgentSet(number = NO_WOLVES, position_dist=d3, size_dist=d4, color=(1,0,0))

# create sprites
fig, ax = plt.subplots()
plt.xlim(0, 10)
plt.ylim(0, 10)

for sheep in sheeps:
    ax.add_patch(sheep.sprite)
    ax.text(sheep.x_pos, sheep.y_pos, 'Sheep', ha='center', va='center')

    for wolf in wolves:
        ax.add_patch(wolf.sprite)
        ax.text(wolf.x_pos, wolf.y_pos, 'Wolf', ha='center', va='center')

plt.savefig('sheep_and_wolves.png')
plt.show()