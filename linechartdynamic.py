import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


fig, ax = plt.subplots()

x = []
y = []

def update(frame):
    x.append(frame)
    y.append(random.randint(0, 10))
    
    ax.clear()
    ax.plot(x, y)
    
    ax.set_title("Dynamic Line Chart")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

ani = animation.FuncAnimation(fig, update, frames=range(20), interval=1000)

plt.show()
