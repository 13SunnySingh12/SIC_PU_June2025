import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

# Scatter Plot
plt.scatter(x, y, color = 'red', marker = "o")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Scatter Plot")
plt.show()