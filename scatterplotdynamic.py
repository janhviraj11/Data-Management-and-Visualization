import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


fig, ax = plt.subplots()

x_data = []
y_data = []

scatter = ax.scatter([], [])

def update(frame):
    
    x_data.append(frame)
    y_data.append(random.randint(0, 50))
    
    ax.clear()
    ax.scatter(x_data, y_data, color='blue')
    
    ax.set_xlim(0, max(20, frame + 1))
    ax.set_ylim(0, 60)
    ax.set_title("Dynamic Scatter Plot")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")


ani = animation.FuncAnimation(fig, update, frames=range(20), interval=1000)

plt.show()
