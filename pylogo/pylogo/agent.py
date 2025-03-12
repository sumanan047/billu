"""Agents in the simulation."""
import uuid
import numpy as np

class Turtle:
  def __init__(self, **kwargs):
    self.id = str(uuid.uuid4())

  def set_prop(self, prop_name, val):
    self.__dict__[prop_name] = val

  def inc_prop(self, prop_name, amount):
    self.__dict__[prop_name] += amount

class TurtleSet:
  def __init__(self, numbers):
    self.numbers = numbers
    self.turtle_dict = {str(uuid.uuid4()): Turtle() for _ in range(numbers)}

  def set_prop_constant(self, prop_name, val):
    for turtle in self.turtle_dict.values():
      turtle.set_prop(prop_name, val)

  def set_prop_uniform(self, prop_name, val1, val2):
    val_arry = np.random.uniform(val1, val2, self.numbers)
    # set values of props on turtle from the array
    for i, turtle in enumerate(self.turtle_dict.values()):
      turtle.set_prop(prop_name, val_arry[i])

  def set_prop_normal(self, prop_name, mean, std):
    val_arry = np.random.normal(mean, std, self.numbers)
    for i, turtle in enumerate(self.turtle_dict.values()):
      turtle.set_prop(prop_name, val_arry[i])

  def set_prop_poisson(self, prop_name, lam):
     val_arry = np.random.poisson(lam, self.numbers)
     for i, turtle in enumerate(self.turtle_dict.values()):
        turtle.set_prop(prop_name, val_arry[i])

  def filter_agents(self, prop, val):
        return [turtle for turtle in self.turtle_dict.values() if turtle.__dict__[prop] == val]

  def filter_agents_greater_than(self, prop, val):
        return [turtle for turtle in self.turtle_dict.values() if turtle.__dict__[prop] > val]

  def filter_agents_less_than(self, prop, val):
        return [turtle for turtle in self.turtle_dict.values() if turtle.__dict__[prop] < val]