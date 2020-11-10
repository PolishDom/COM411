import matplotlib.pyplot as plt

def coordinate():
  xvalue = input("Please enter a x value")
  yvalue = input("Please enter a Y value")
  x_and_y_values = (xvalue , yvalue)
  return x_and_y_values

def path():
  print ("Retrieving path...")
  x_values = []
  y_values = []
  x = range(4)
  for i in x:
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]

def run():
  values = path()
  plt.plot(values[0],values[1] , "ro--")
  plt.show()

run()






