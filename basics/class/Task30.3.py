class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def ageup(self):
    self.age += 1 


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()

class Human:

  MAX_ENERGY = 100

  def __init__(self):

    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def ageup(self):
    self.age += 1

  def displayageup(self):
    human.ageup()
    print (f"Your Human age is {self.age}")

  def eat(self):
    self.energy += 1 

  def move(self):
    self.energy -= 1

  def displayname(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.displayname()

humanuserinput = input("Would you like to enter the move,eat or age regime? y/n ")

while humanuserinput != "n":
  whichone = input("Would you like to age up , eat for extra energy or move to decrease your energy?age / eat / move")

  if whichone == "age":
    print ("Your human age has increased")
    human.displayageup()
  elif whichone == "eat":
    
    


