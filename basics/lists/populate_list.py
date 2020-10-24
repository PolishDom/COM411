def movements():
  directions = ["Move forward" , "Move Backward", "Move Left", "Move Right"]
  return directions

def menu():
  print("Please enter a direction: ")
  Move = movements()

  for index in range(len(Move)):
    print("{}: {}" .format(index, Move[index]))

  direction_index = int(input())

  return Move[direction_index]

def run():
  route = []
  print ("Working out escape route...")
  for count in range(5):
    movements = menu()
    route.append(movements)

  print("Escape Route: {}".format(route))


print (run())