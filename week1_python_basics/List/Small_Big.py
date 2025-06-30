# Find smallest and biggest elements in an list of n numbers.

def find_smallest_and_biggest(numbers):
    
    if len(numbers) == 0:
        print("No numbers entered.")
        return None

    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    unique_numbers.sort()
    print("Sorted list without duplicates:", unique_numbers)

    smallest = unique_numbers[0]
    largest = unique_numbers[-1]

    print(f"{smallest} is the smallest element in the list.")
    print(f"{largest} is the biggest element in the list.")


input_numbers = list(map(int, input("Enter the numbers: ").split()))
print("Original list:", input_numbers)

find_smallest_and_biggest(input_numbers)
