#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2

def fibonacci(number):
    if number <= 0:
        return "Number should be greater than 0. "
    elif number == 1:
        return 1
    elif number == 2:
        return 2 
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


term_number = int(input("Enter the term number: "))
if term_number <= 0:
    print(fibonacci(term_number))
else:
    print("The", term_number,"th Fibonacci number is:", fibonacci(term_number))
