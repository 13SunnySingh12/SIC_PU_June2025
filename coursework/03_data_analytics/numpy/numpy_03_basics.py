# What .shape reports for a vector (1D), a matrix (2D) and a tensor (3D).

import numpy as np

vector = np.arange(5)
print('Vector shape:', vector.shape)

matrix = np.ones([3, 2])
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3])
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape)