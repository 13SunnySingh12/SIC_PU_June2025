# Heatmap: rendering a 2D array as colour with imshow, plus a colour bar.

import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(10,10)

plt.imshow(data, cmap = 'coolwarm', interpolation = 'nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()