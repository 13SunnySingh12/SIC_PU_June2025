
import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [50, 25, 89, 45]

# Bar Graph
plt.bar(categories, values, color = ['red', 'blue', 'green', 'grey'])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Bar Plot")
plt.show()
