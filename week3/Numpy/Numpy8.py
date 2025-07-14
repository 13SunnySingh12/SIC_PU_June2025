import numpy as np

matrix1 = np.array([[3, 4, 5], [2, 6, 9]])   # Shape: (2, 3)

matrix2 = np.array([[3, 4], [3, 5], [2, 6]])      # Shape: (3, 2)

matrix3 = np.dot(matrix1, matrix2)  # Result: Shape (2, 2)

print('Matrix3=\n', matrix3)

'''
-> Row 0 x Column 0:
(3x3) + (4x3) + (5x2) = 9 + 12 + 10 = 31

-> Row 0 x Column 1:
(3x4) + (4x5) + (5x6) = 12 + 20 + 30 = 62

-> Row 1 x Column 0:
(2x3) + (6x3) + (9x2) = 6 + 18 + 18 = 42

-> Row 1 x Column 1:
(2x4) + (6x5) + (9x6) = 8 + 30 + 54 = 92
'''