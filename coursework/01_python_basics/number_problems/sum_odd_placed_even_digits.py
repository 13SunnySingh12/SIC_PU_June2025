#Find sum of the Odd placed Even digits in the given number.

def sum_odd_placed_even_digits(number):
    number_str = str(number) 
    total = 0
    for i in range(0, len(number_str), 2):
        digit = int(number_str[i])
        if digit % 2 == 0:
            total+=digit
    return total

num = int(input("Enter a number: "))
print("sum of the Odd placed Even digits is:",sum_odd_placed_even_digits(num))
