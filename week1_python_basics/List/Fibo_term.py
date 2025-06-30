#Print N Fibo terms with 1 and 2 as 1st 2 terms.

def hema_fibo(n):
    if n <= 0:
        print("Number should be greater than 0.")
        return 0
    
    elif n == 1:
        return 1

    elif n == 2:
        return 2
    
    else:
        return hema_fibo(n - 1) + hema_fibo(n - 2)

num_terms = int(input("Enter how many Fibonacci terms you want: "))
print(f"First {num_terms} Fibonacci terms are:")
for i in range(1, num_terms + 1):
    print(hema_fibo(i), end=' ')