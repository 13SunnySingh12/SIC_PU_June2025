# Bubble Sort

def Bubble_Sort(arr_numbers, length_arr):

    for i  in range (length_arr):
        for j  in range (length_arr - i - 1 ):
            if arr_numbers[j] > arr_numbers[j + 1]:
                temp = arr_numbers[j]
                arr_numbers[j] = arr_numbers[j + 1]
                arr_numbers[j + 1] = temp
    return arr_numbers

arr_numbers = list(map(int, input("Enter numbers to be sort sorted: ").split()))
print("Unsorted array:", arr_numbers)
length_arr = len(arr_numbers)

print("Sorted array:", Bubble_Sort(arr_numbers, length_arr) )