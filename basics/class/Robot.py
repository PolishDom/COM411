class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  #initializer
  def __init__(self):
    #Instance attributes
    self.name = "Robot"
    self.age = 0
    self.energy = 0 

  #instance methods
  def display(self):
    print(f"I am {self.name}, age {self.age} and my energy level is {self.energy}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

