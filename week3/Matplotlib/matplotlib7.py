import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate 50 random values for x, y, and z
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# Create 3D figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D scatter plot
ax.scatter(x, y, z, color='red')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Scatter Plot")
plt.show()