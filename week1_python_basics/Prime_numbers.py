# Print the Prime numbers in decreasing order between m and n (m < n)

def is_prime(number):
    
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

m = int(input("Enter the smaller number (m): "))
n = int(input("Enter the larger number (n): "))

for i in range(n, m - 1, -1):
    if is_prime(i):
        print(i, end=" ")
