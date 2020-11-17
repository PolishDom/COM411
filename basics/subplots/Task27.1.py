import matplotlib.pyplot as plt

def read_data(filepathname):
  data = []
  with open("basics/subplots/temps.txt") as file:
    temps = file.readlines()
    print (temps)
    for line in temps:
      print(f"{line}")
      
      data.append(int(line.strip()))
  return data

def run():
  data = read_data('basics/subplots/temps.txt')
  fix, axs = plt.subplots(1, 1)
  #x = range(0, 7, 1)
  #y = data

  axs.set_xlabel("day")
  axs.set_ylabel("temperature")

  axs.plot(data)

  plt.tight_layout()
  plt.show()

run()
