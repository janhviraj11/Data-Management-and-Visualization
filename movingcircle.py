import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

def update(frame):
 
    circle.center = (frame * 0.5, 5)  
    return circle,


ani = animation.FuncAnimation(fig, update, frames=20, interval=200, blit=True)

plt.show()
