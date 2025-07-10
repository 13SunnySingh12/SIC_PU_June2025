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

# ------------------ full() ------------------
array4 = np.full((2, 4), 5)
array5 = np.full((1, 5), 10)
print("array4:\n", array4)
print("array5:\n", array5)

# ------------------ arange() ------------------
a1 = np.arange(10)
a2 = np.arange(10, 20)
a3 = np.arange(10, 30, 3)

print("a1:", a1)
print("a2:", a2)
print("a3:", a3)

# ------------------ ones() ------------------
o1 = np.ones(10)
o2 = np.ones((2, 8))
o3 = np.ones((3, 5))

print("o1:", o1)
print("o2:\n", o2)
print("o3:\n", o3)

# ------------------ Shapes ------------------
vector = np.arange(5)
matrix = np.ones([3, 2])
tensor = np.zeros([2, 3, 3])

print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)
print("Tensor shape:", tensor.shape)

# ------------------ Reshape ------------------
arr = np.arange(1, 10)
print("Original 1D array:", arr)

arr = arr.reshape(3, 3)
print("Reshaped 3x3:\n", arr)

arr = arr.reshape(9)
print("Flattened:", arr)

# ------------------ Multiple Reshape ------------------
arr1 = np.arange(12)
print("Original arr1:", arr1)

arr2 = arr1.reshape(2, 6)
arr3 = arr1.reshape(6, 2)
arr4 = arr1.reshape(3, 4)
arr5 = arr1.reshape(12, 1)
arr6 = arr1.reshape(4, 3)

print("arr2 (2x6):\n", arr2)
print("arr3 (6x2):\n", arr3)
print("arr4 (3x4):\n", arr4)
print("arr5 (12x1):\n", arr5)
print("arr6 (4x3):\n", arr6)

# ------------------ Reshape with -1 ------------------
arr7 = np.arange(1, 10).reshape(3, -1)
print("arr7 reshape (3, -1):\n", arr7)

arr8 = np.arange(2, 25, 2)  # 12 elements

arr9 = arr8.reshape(4, -1)
arr10 = arr8.reshape(2, -1)
arr11 = arr8.reshape(3, -1)
arr12 = arr8.reshape(-1, 4)

print("arr9 (4 rows):\n", arr9)
print("arr10 (2 rows):\n", arr10)
print("arr11 (3 rows):\n", arr11)
print("arr12 (4 cols):\n", arr12)

# ------------------ Manual Shape Setting ------------------
array6 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])
print("Original shape:", array6.shape)

array6.shape = (6, 2)
print("Shape (6, 2):\n", array6)

array6.shape = (3, 4)
print("Shape (3, 4):\n", array6)

array6.shape = (4, 3)
print("Shape (4, 3):\n", array6)

# ------------------ Matrix Multiplication ------------------
matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)
print("Matrix multiplication result:\n", matrix3)

# ------------------ Broadcasting ------------------
broadcast_array = np.array([2, 4, 6, 8, 9, 19])
broadcast_result = broadcast_array + 5

print("Original array:", broadcast_array)
print("After broadcasting (add 5):", broadcast_result)
