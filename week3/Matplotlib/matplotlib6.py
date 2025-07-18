import numpy as np
import matplotlib.pyplot as plt

data = [np.random.randn(100) for _ in range(4)]

# Box Plot
plt.boxplot(data, patch_artist = True)
plt.xlabel("Category")
plt.ylabel("Vlaues")
plt.title("Box Plot")
plt.show()

#Violin Plot
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()