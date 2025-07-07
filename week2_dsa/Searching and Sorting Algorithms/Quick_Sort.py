# Quick Sort

def Quick_Sort(array, low, high):
    if low < high:
        pivot_index = Partition(array, low, high)
        Quick_Sort(array, low, pivot_index - 1)
        Quick_Sort(array, pivot_index + 1, high)

def Partition(array, low, high):

    pivot = array[high]
    pivot_index = low

    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1


    array[pivot_index], array[high] = array[high], array[pivot_index]

    return pivot_index

array_size = int(input("Enter the length of array: "))
array = list(map(int,input("Enter the elements: ").split()))
print("Unsorted array:", array)
low = 0
high = array_size - 1
Quick_Sort(array, low, high)
print("Sorted array:", array)

