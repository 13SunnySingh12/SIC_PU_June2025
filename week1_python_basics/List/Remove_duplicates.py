# Remove the duplicates in a list of size n

def remove_duplicates(numbers):

    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("List after removing duplicates:", unique_numbers)

input_numbers = list(map(int, input("Enter the numbers: ").split()))
print("Original list:", input_numbers)

remove_duplicates(input_numbers)
