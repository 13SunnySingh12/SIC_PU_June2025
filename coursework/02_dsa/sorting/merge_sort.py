# Merge Sort - split the list in half, sort each half, merge them back.


def Merge(array, left_half, right_half):
    i = j = k = 0

    # Take whichever half currently has the smaller front element.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    # One half is now exhausted; copy whatever is left of the other.
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

    return array


def Merge_Sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    Merge_Sort(left_half)
    Merge_Sort(right_half)

    return Merge(array, left_half, right_half)


array_length = int(input("Enter the length of array: "))
array = list(map(int, input("Enter the elements: ").split()))
print("Unsorted array:", array)
Merge_Sort(array)
print("Sorted array:", array)
