# Find the smallest of 3 distinct numbers

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Check if all numbers are distinct
if first_number != second_number and second_number != third_number and first_number != third_number:
    
    # Determine the smallest number
    if first_number < second_number and first_number < third_number:
        smallest_number = first_number
    elif second_number < third_number:
        smallest_number = second_number
    else:
        smallest_number = third_number

    print(smallest_number,"is the smallest of the 3 distinct numbers.")
else:
    print("Please enter 3 distinct numbers.")


