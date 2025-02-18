from pylogo.agent import Agent, AgentSet
from pylogo.simulation import simulation, Time
from pylogo.rules import move_by_at_angle, move_up
from pylogo.distributions import Distribution_2D, Distribution_1D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# create distributions
d1 = Distribution_2D()
d1.uniform(low=[-15,0], high=[1,7], size=100)
d2 = Distribution_2D()
d2.uniform(low=[0.5,0.5], high=[0.5,0.5], size=100)
d3 = Distribution_1D()
d3.normal(mean=33, std=10, size=100)

# make an agent
ag1 = Agent()
# unwrap d1.x_arr and d1.y_arr to fill AgentSet positions
# ag1 = AgentSet(number = 100, position_dist=d1, size_dist=d2, age=d3)
# ag_list = ag1.make_agents(position_dist=d1, size_dist=d2, color=(1,0,0))

# make a time object
# _t = Time(0, 10, 0.1)
# # make a simulation
# sim = simulation({ag1: [move_by_at_angle]}, _t)
# sim.run_simulation(distance=1, angle=0.1)
# sim.save_simulation()




# plot the simulation
# read the data from the file simulation.csv
data = pd.read_csv('simulation.csv')
x = []
y = []
import matplotlib.animation as animation

fig, ax = plt.subplots()
x_lim = 1000
y_lim = 1000
ax.set_xlim(-x_lim,y_lim)
ax.set_ylim(-x_lim,y_lim)
ax.set_aspect('equal')
line, = ax.plot([], [], 'r-')

def animate(i):
    move_by_at_angle(ag1, distance=i**0.1, angle=np.pi/3*i**2)
    x.append(ag1.x_pos)
    y.append(ag1.y_pos)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=4, interval=1)
ani.save('animation.gif', writer='pillow')
plt.show()