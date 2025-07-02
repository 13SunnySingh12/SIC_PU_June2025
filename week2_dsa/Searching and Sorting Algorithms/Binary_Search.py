#Implement Binary Search using While True.

def binary_Search(arr_numbers, target_element):
    low = 0
    high = len(arr_numbers) - 1

    while True:

        if low > high:
            return -1
        else:    
            mid = (low + high) // 2

        if arr_numbers[mid] == target_element:
            return mid
        
        elif arr_numbers[mid] < target_element:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr_numbers = list(map(int,input("Enter the array of elements: ").split()))

print(arr_numbers)

target_element = int(input("Enter the element to be found: "))

target_index = binary_Search(arr_numbers, target_element)

if target_index != -1:
    print("Element found at index:", target_index)
else:
    print("Element not found!")