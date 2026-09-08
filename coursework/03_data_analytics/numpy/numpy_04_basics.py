# Reshaping an array, and the rule behind it: the new shape must hold exactly
# as many elements as the old one. The last reshape breaks that rule on purpose.

import numpy as np

arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9)
print(arr)

# Deliberate failure: 9 elements cannot be laid out as 2x5, so reshape raises.
# Caught here so the demonstration above still runs to completion.
try:
    arr = arr.reshape(2, 5)
    print(arr)
except ValueError as error:
    print('reshape(2, 5) on 9 elements ->', type(error).__name__, '-', error)