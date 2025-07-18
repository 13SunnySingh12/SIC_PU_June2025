import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line Graph
plt.plot(x, y, label = "Sine Wave")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Sine Wave")
plt.legend()
plt.show()