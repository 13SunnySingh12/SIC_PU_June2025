#Find biggest digit in a number

def biggest_digit(number):
    digits = []
    unique_digits = []

    for digit in str(number):
        digits.append(int(digit))

    for d in digits:
        if d not in unique_digits:
            unique_digits.append(d)

    unique_digits.sort()

    if len(unique_digits) >= 2:
        print(unique_digits[-1], "is the biggest digit in a number.")
    else:
        print("The number should have atleast two unique digits.")

num = int(input("Enter a number: "))
biggest_digit(num)
