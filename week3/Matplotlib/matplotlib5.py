import numpy as np
import matplotlib.pyplot as plt

size = [30, 50, 20, 5]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'grey']

# Pie Chart
plt.pie(size, labels = labels, colors = colors, autopct = "%1.1f%%", startangle = 140)
plt.title("Pie Chart")
plt.show()