def movements():
  directions = ["Move forward" , "Move Backward", "Move Left", "Move Right"]
  return directions

def menu():
  print("Please enter a direction: ")
  variable = movements()
  for index in range(len(variable)):
    print("{}: {}" .format(index, variable[index]))

def run():
  print (menu())

print (run())