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

array1.shape = (4, 2) # Error New shape of the array must consist of same number of elements as that of original array
print(array1.shape)
print(array1)