# Reshaping by assigning to .shape instead of calling reshape. The same
# element-count rule applies, and the last assignment breaks it on purpose.

import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])
print(array1.shape)
print(type(array1))
print(array1)

array1.shape = (6, 2)
print(array1.shape)
print(array1)

array1.shape = (3, 4)
print(array1.shape)
print(array1)

array1.shape = (4, 3)
print(array1.shape)
print(array1)

# Deliberate failure: a new shape must hold exactly as many elements as the
# original array (12 here), and 4x2 only holds 8.
try:
    array1.shape = (4, 2)
    print(array1.shape)
    print(array1)
except ValueError as error:
    print('shape = (4, 2) on 12 elements ->', type(error).__name__, '-', error)