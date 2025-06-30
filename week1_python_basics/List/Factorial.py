# Find Factorial of a number(Using recursion)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
input_number = int(input("Enter a number:"))
print(f"Factorial of {input_number} is:", factorial(input_number))