from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt 

import random

class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return (f"universe(planets= {self.planets})")

  def __str__(self):
    return (f"The universe contains {len(self.planets)} planets")

  def generate(self):
    planet = Planet()

    num_humans = random.randit(0, 100)
    num_robots = random.randit(0, 100)

    for count in range(num_humans):
      human = Human()
      planet.add_human(human)

    for count in range(num_robots):
      robot = Robot()
      planet.add_robot(robot)

    for index in range(random.randint(1,10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(human)

    for index in range(random.randint(1,10)):
      human = Human(f"Human{index}")
      planet.add_human(human)
    
    self.planets.append(planet)

  def show_populations