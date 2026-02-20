import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x_data = []
y_line = []
y_bar = []

def update(frame):
   
    x_data.append(frame)
    y_line.append(random.randint(0, 20))
    y_bar.append(random.randint(0, 20))
    
    
    ax1.clear()
    ax1.plot(x_data, y_line, marker='o', color='blue')
    ax1.set_title("Dynamic Line Plot")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_xlim(0, max(10, frame))
    ax1.set_ylim(0, 25)
    
    
    ax2.clear()
    ax2.bar(range(len(y_bar)), y_bar, color='green')
    ax2.set_title("Dynamic Bar Chart")
    ax2.set_xlabel("Index")
    ax2.set_ylabel("Value")
    ax2.set_ylim(0, 25)


ani = animation.FuncAnimation(fig, update, frames=20, interval=1000)

plt.tight_layout()
plt.show()
