import matplotlib.pyplot as plt


labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)


plt.title("Static Pie Chart Example")


plt.show()
