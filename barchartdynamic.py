import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


categories = ['A', 'B', 'C', 'D']
values = [0, 0, 0, 0]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    for i in range(len(values)):
        values[i] = random.randint(0, 50)
    
    ax.bar(categories, values, color='skyblue')
    
    ax.set_title("Dynamic Bar Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")
    ax.set_ylim(0, 50)


ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()
