import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from pylogo import agent, distributions

d1 = distributions.Distribution_2D()
d1.uniform(low=[0,1], high=[10,7], size=100)
d2 = distributions.Distribution_2D()
d2.uniform(low=[0.1,0.1], high=[0.1,0.1], size=100)

ags = agent.AgentSet(number = 100, position_dist=d1, size_dist=d2)

fig, ax = plt.subplots()
plt.xlim(0, 10)
plt.ylim(0, 10)

for ag in ags:
    ax.add_patch(ag.sprite)


plt.show()