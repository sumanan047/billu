import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from pylogo.agent import Agent, AgentSet
from pylogo.distributions import Distribution_1D, Distribution_2D
from pylogo.simulation import Simulation, Time
from pylogo.rules import move_by_at_angle, move_up, move_randomly

NO_AGENTS = 5

# make distributions
d1 = Distribution_2D()
d1.uniform(low=[-20,-20], high=[50,70], size=NO_AGENTS)

d2 = Distribution_2D()
d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=NO_AGENTS)
# make an agent
ag = Agent()
agset = AgentSet(number = NO_AGENTS, position_dist=d1, size_dist=d2, color=(1, 0, 0))
_t = Time(0, 10, 1)

fig, ax = plt.subplots(figsize=(10, 10))
x_lim = 100
y_lim = 100
ax.set_aspect('equal')
ax.set_xlim(-x_lim, y_lim)
ax.set_ylim(-x_lim, y_lim)
x = []
y = []

def update(frame):
    ax.clear()
    ax.set_xlim(-x_lim, y_lim)
    ax.set_ylim(-x_lim, y_lim)
    ax.set_aspect('equal')
    sim = Simulation({agset: [move_randomly]}, _t)
    sim.run_simulation(distance_range=[0,10], angle=[0, 2*np.pi])
    ax.plot([ag.x_pos for ag in agset.agents], [ag.y_pos for ag in agset.agents], 'rx')

ani = animation.FuncAnimation(fig, update, frames=100, interval=100, repeat=False)

ani.save('animation.gif', writer='pillow')
plt.show()