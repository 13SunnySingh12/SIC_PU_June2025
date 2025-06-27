##Print the 'X' shape by accepting number of lines

def x_shape(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

lines = int(input("Enter number of lines for X Shape: "))
x_shape(lines)
