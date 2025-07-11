import numpy as np

array = np.array([2, 4, 6, 8, 9, 19])

array2 = array + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array)
print(array2)

array1 = np.array([[2, 4, 6, 8], [9, 19, 4, 10]])

array3 = array1 + 5 # Broadcasting. Adding a scalar quantity to every element of the array

print(array1)
print(array3)
