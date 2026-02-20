import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


labels = ['Apples', 'Bananas', 'Cherries', 'Dates']


data = [10, 10, 10, 10]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
  
    new_data = [random.randint(5, 30) for _ in data]
    
    ax.pie(new_data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart")


ani = animation.FuncAnimation(fig, update, interval=1000) 

plt.show()
