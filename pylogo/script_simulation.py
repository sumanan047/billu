import matplotlib.pyplot as plt
import numpy as np
from pylogo.agent import Agent
from pylogo.simulation import simulation, Time
from pylogo.rules import move_by_at_angle, move_up

# make an agent
ag = Agent()
_t = Time(0, 10, 0.1)
# make a simulation
sim = simulation({ag: [move_by_at_angle, move_up]}, _t)
sim.run_simulation(distance=1, angle=np.pi/10)
sim.save_simulation()