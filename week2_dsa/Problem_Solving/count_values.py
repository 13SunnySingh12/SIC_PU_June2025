




def count_values_p(arr):
    arr.sort()
    print(arr)
    count = 0

    for y in range (1, len(arr)-1):
        if arr[y] > arr[y - 1]:
            count += arr[y] - arr[y - 1] -1

    return count

arr = list(map(int,input("Enter array elements: ").split()))

result = count_values_p(arr)

print("Number of p values: ",result)