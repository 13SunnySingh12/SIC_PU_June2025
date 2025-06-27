#Print the Hollow Square by accepting number of lines

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

lines = int(input("Enter number of lines for Hollow Square: "))
hollow_square(lines)
