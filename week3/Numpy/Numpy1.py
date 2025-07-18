import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print("Array1:", array1)
print("Array2:\n", array2)
print("Array3:\n", array3)

print("array1[0], array1[2]:", array1[0], array1[2])
print("array2[0][0], array2[0][3]:", array2[0][0], array2[0][3])
print("array3[1][0], array3[1][3]:", array3[1][0], array3[1][3])

print("Type of array1:", type(array1))
print("Type of array2:", type(array2))
print("Type of array1[0]:", type(array1[0]))
print("Type of array2[0]:", type(array2[0]))
print("Type of array2[0][0]:", type(array2[0][0]))
