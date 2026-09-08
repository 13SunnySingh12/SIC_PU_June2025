# Insertion sort

def Insertion_Sort(array, array_length):
    for i in range(1, array_length):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

array_length = int(input("Enter the length of array: "))
array = list(map(int,input("Enter the elements: ").split()))
print("Unsorted array:", array)
Insertion_Sort(array, array_length)
print("Sorted array:", array)
