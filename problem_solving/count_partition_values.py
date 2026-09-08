'''
You are given an array of n integers. You have to divide this array into two parts of size x and y such that x + y = n.

The condition is:

1) All elements in the first part (of size x) must be greater than a number p

2) All elements in the second part (of size y) must be less than that same number p

You are allowed to choose x and y (any values such that x + y = n and both are ≥ 1).

Your task is to determine how many possible integer values of p satisfy this condition.

'''



def count_values_p(arr, y):
    # Sorted, the y smallest elements form the second part and must all be
    # below p, while the rest must all be above it - so p can be any integer
    # strictly between arr[y - 1] and arr[y].
    arr.sort()
    print(arr)

    if arr[y] > arr[y - 1]:
        p = arr[y] - arr[y - 1] - 1
    else:
        p = 0

    return p

n, x, y = map(int, input("Enter elements: ").split())
arr = list(map(int, input("Enter array elements: ").split()))

print("Number of p values:", count_values_p(arr, y))
