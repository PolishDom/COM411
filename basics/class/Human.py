class Human:

  #Class attribute
  MAX_ENERGY = 100

  #initializer
  def __init__(self):

    #Instance attributes
    self.name = "Human"
    self.age = 0
    self.energy = self.MAX_ENERGY 

  #instance methods
  def grow(self):
    self.age += 1

  def eat(self, eating):
    eatingamount = self.energy + eating
    if (eatingamount > Robot.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
      return eatingamount - self.energy
    else:
      self.energy = eatingamount
      return 0
  
  def move(self, distance):
    eatingamount = self.energy - distance
    if (eatingamount < 0):
      self.energy = 0
      return self.energy - abs(eatingamount)
    else:
      self.energy = eatingamount
      return 0 

  def display(self):
    print(f"I am {self.name}, age {self.age} and my energy level is {self.energy}")

  

if (__name__ == "__main__"):
  human = Human()
  human.display()

