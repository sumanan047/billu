import pytest
import numpy as np
from pylogo.simulation import Time, simulation
from pylogo.agent import Agent
from pylogo.rules import move_by_at_angle, move_up, move_down, move_left, move_right


@pytest.fixture
def agent1():
    return Agent()

@pytest.fixture
def agent2():
    return Agent()

def test_time_array():
    t = Time(0, 10, 0.1)
    time_array = t.time_array()
    assert len(time_array) == 100
    assert time_array[0] == 0
    assert time_array[-1] == 9.9

def test_time_iter():
    t = Time(0, 10, 0.1)
    for time in t:
        assert time >= 0
        assert time <= 10

def test_time_next():
    t = Time(0, 10, 0.1)
    time = next(t)
    assert time == 0.1
    time = next(t)
    assert time == 0.2

def test_time_str():
    t = Time(0, 10, 0.1)
    assert str(t) == "Time object with start_time: 0, end_time: 10, time_step: 0.1"

def test_simulation_init():
    with pytest.raises(ValueError):
        sim = simulation({}, Time(0, 10, 0.1))


def test_simulation_run_simulation(agent1, agent2):
    sim_agent_rules = {
        agent1: [move_by_at_angle, move_up],
        agent2: [move_down, move_left]
    }
    sim = simulation(sim_agent_rules, Time(0, 10, 0.1))
    sim.run_simulation(distance=1, angle=np.pi/10)
    assert sim.data is not None