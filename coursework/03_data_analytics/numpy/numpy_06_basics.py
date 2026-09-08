# Passing -1 to reshape lets numpy work that dimension out. Only one dimension
# may be left unknown - the last reshape breaks that rule on purpose.

import numpy as np

arr = np.arange(1, 10).reshape(3, -1) # Here python infers/decides the number of columns by itself.
print(arr)

arr1 = np.arange(1, 10)
arr2 = np.arange(2, 25, 2)
arr3 = arr1.reshape(3, -1)
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows

# Deliberate failure: only ONE dimension may be left for numpy to infer.
# Caught here so the successful reshapes above still print.
try:
    arr8 = arr2.reshape(-1, -1)
except ValueError as error:
    arr8 = None
    print('reshape(-1, -1) ->', type(error).__name__, '-', error)

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
print('Arr7:\n', arr7)
print('Arr8:\n', arr8)   # None - the reshape above could not be performed