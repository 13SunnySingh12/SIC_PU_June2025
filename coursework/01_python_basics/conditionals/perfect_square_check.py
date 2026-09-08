# Check if a positive integer is a perfect square

input_number = int(input("Enter a positive number: "))

square_root = int(input_number ** 0.5)

if square_root ** 2 == input_number:
    print(input_number, "is a Perfect Square.")
else:
    print(input_number, "is not a Perfect Square.")

