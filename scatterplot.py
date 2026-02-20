import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 20]


plt.scatter(x_values, y_values, color='red', marker='o')


plt.title("Static Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")


plt.show()
