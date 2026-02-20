import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()

data = []

def update(frame):
    ax.clear()
    
    
    new_value = np.random.randint(0, 10)
    data.append(new_value)
    
   
    ax.hist(data, bins=10, color='skyblue', edgecolor='black')
    
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


ani = animation.FuncAnimation(fig, update, frames=20, interval=1000)

plt.show()
