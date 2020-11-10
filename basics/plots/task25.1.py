import matplotlib.pyplot as plt

def display (xvalues,yvalues):
  plt.plot(xvalues,yvalues)
  plt.show()


def run():
  x_values = [1,2,3,4,5]
  y_values = [1,4,9,16,25]
  dis = display(x_values,y_values)

run()