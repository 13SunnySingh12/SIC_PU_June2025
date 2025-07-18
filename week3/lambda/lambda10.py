from functools import reduce

numbers = [1, 2, 3, 4]

# Compute the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)
