#Find 2nd smallest digit in a number

def second_smallest_digit(number):
    digits = []
    unique_digits = []

    for digit in str(number):
        digits.append(int(digit))

    for d in digits:
        if d not in unique_digits:
            unique_digits.append(d)

    unique_digits.sort()

    if len(unique_digits) >= 2:
        print(unique_digits[1], "is the 2nd smallest digit in the number.")
    else:
        print("The number doesn't have at least two unique digits.")

num = int(input("Enter a number: "))
second_smallest_digit(num)
