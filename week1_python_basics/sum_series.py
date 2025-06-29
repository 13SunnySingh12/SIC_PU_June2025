#Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)

def sum_series(m,n):
    total = 0
    for i in range(m):
        numerator = n ** (2 ** i)
        denominator = 2 * i + 1
        sign = (-1) ** i
        term = (sign) * (numerator / denominator)
        total += term
    return total

n = int(input("Enter term value (n): "))
m = int(input("Enter number of terms(m): "))

print("sum of the series: ",sum_series(m,n))