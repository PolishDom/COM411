class Person:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight
        
  def display(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight}kg")

prins = Person("Prins", 36, 85)

prins.display()