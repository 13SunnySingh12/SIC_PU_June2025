# Selection Sort

def Selection_sort(array_numbers, array_length):

    for i in range(array_length):
        min_index = i

        for j in range(i + 1, array_length):
            if array_numbers[min_index] > array_numbers[j]:
                min_index = j

        if min_index != i:
            temp =  array_numbers[i]
            array_numbers[i] = array_numbers[min_index]
            array_numbers[min_index] = temp
    
    return array_numbers

array_numbers = list(map(int, input("Enter numbers to be sort sorted: ").split()))
print("Unsorted array:", array_numbers)
array_length = len(array_numbers)
print(("Sorted array:"), Selection_sort(array_numbers, array_length))