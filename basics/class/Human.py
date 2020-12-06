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
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.display()

