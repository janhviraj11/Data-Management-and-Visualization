import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))


ax1.plot(x, y1, marker='o', color='blue')
ax1.set_title("Line Plot 1")
ax1.set_xlabel("X")
ax1.set_ylabel("Y1")


ax2.bar(x, y2, color='green')
ax2.set_title("Bar Plot 2")
ax2.set_xlabel("X")
ax2.set_ylabel("Y2")

plt.tight_layout()


plt.show()
