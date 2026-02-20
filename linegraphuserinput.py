import matplotlib.pyplot as plt


x_input = input("Enter X values separated by commas: ")
y_input = input("Enter Y values separated by commas: ")


x_values = [float(x) for x in x_input.split(',')]
y_values = [float(y) for y in y_input.split(',')]


if len(x_values) != len(y_values):
    print("Error: X and Y must have the same number of values.")
else:

    plt.plot(x_values, y_values, marker='o', color='blue')
    
    plt.title("Line Graph from User Input")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    
    
    plt.show()
