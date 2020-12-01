class Planet:

  def lists(self):
    humans = []
    robots = []

  def add_human(self, human):
    humans.append(human)

  def remove_human(self, human):
    humans.remove(human)

  def add_robot(self, robot):
    robots.append(robot)

  def remove_robot(self, robot):
    robots.remove(robot)

  def display(self):
    print (humans)
    print (robots)


Planet.display()

if (__name__ == "__main__"):
  planet = Planet()
  planet.__repr__()