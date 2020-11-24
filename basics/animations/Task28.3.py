import numpy as np
import matplotlib.pyplot as plt   
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame_number):
  ax.set_xlim(0,720)
  ax.set_ylim(-1,1)
  x = np.arange(0, frame_number)
  y_values_calculated = np.sin(x * (np.pi/180))
  ax.plot(x,y_values_calculated, 'ro')

def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig,animate, frames = 720, interval = 10)
  plt.show()

run()