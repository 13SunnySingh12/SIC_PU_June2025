# reduce() with a lambda to collapse a list into a single value (the product).

from functools import reduce

numbers = [1, 2, 3, 4]

# Compute the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)
