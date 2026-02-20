import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


fig, ax = plt.subplots()
x_data = []
y_data = []

line, = ax.plot([], [], color='blue', marker='o')


ax.set_xlim(0, 20)
ax.set_ylim(0, 50)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Animated Line Chart")

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 50))
    
  
    line.set_data(x_data, y_data)
    
   
    if frame > 20:
        ax.set_xlim(frame - 20, frame)
    
    return line,


ani = animation.FuncAnimation(fig, update, frames=range(50), interval=500, blit=True)

plt.show()
