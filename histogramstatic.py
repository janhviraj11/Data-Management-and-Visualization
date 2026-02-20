import matplotlib.pyplot as plt


data =[10,12,15,18,20,22,25,25,28,30,30,32,35,38,40]
plt.hist(data,bins=5)
plt.xlabels("values")
plt.ylabels("frequency")
plt.title("static histogram")
plt.show()