#Print the Hollow Rhombus by accepting number of lines

def hollow_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

lines = int(input("Enter number of lines for Hollow Rhombus: "))
hollow_rhombus(lines)
