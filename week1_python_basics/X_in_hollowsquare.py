#Print the "X" in Hollow Square by accepting number of lines

def x_in_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

lines = int(input("Enter number of lines for X in Hollow Square: "))
x_in_hollow_square(lines)
