#Implement Binary Search using recursion.

arr_numbers = list(map(int,input("Enter the array of elements: ").split()))
print(arr_numbers)

def binary_Search(arr_numbers, target_element, low , high):
    
        if low > high:
            return -1
        else:    
            mid = (low + high) // 2

        if arr_numbers[mid] == target_element:
            return mid
        
        elif arr_numbers[mid] < target_element:
            return binary_Search(arr_numbers, target_element, mid + 1 , high)

        else:
             return binary_Search(arr_numbers, target_element, low , mid -1)


low = 0
high = len(arr_numbers) - 1
target_element = int(input("Enter the element to be found: "))
target_index = binary_Search(arr_numbers, target_element, low , high)

if target_index != -1:
    print("Element found at index:", target_index)
else:
    print("Element not found!")