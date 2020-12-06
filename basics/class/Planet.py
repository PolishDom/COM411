class Planet:

  def __init__(self):

    self.humans = []
    self.robots = []

  def add_human(self, human):
    self.humans.append(human)

  def remove_human(self, human):
    self.humans.remove(human)

  def add_robot(self, robot):
    self.robots.append(robot)

  def remove_robot(self, robot):
    self.robots.remove(robot)

  def display(self):
    print(f"This is the lists as follows, Humans: {self.humans}, Robots: {self.robots}")

planet_pluto = Planet()
dominik = human("Dominik")
dominik_the_robot = robot("DominikRobot")
planet_pluto.add_robot(dominik_the_robot)
planet_pluto.add_human(dominik)

# With DICTIONAIRY INSTEAD

class Planet:

  def __init__(self):
    self.inhabitants = {
      "humans" : [],
      "robots" : []
    }

  def add_human(self, human):
    self.inhabitants["humans"].append(human)

  def remove_human(self, human):
    self.inhabitants["humans"].remove(human)

  def add_robot(self, robot):
    self.inhabitants["robots"].append(robot)

  def remove_robot(self, robot):
    self.inhabitants["robots"].remove(robot)

  def display(self):
    print(f"This is the lists as follows, Humans: {self.humans}, Robots: {self.robots}")

planet_pluto = Planet()
dominik = human("Dominik")
dominik_the_robot = robot("DominikRobot")
planet_pluto.add_robot(dominik_the_robot)
planet_pluto.add_human(dominik)
