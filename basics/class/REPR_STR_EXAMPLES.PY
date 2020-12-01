#REPR IS FORMAL STRING
def __repr__(self):
  return f'robot(name={self.name}, age={self.age})'

#STR IS INFORMAL STRING
def __str__(self):
  return f'My name is {self.__name} and I am {self.age} years old.'
