import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

# Histogram
plt.hist(data, bins = 20, color = 'blue', edgecolor = 'black')
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.title("Histogram")
plt.show()