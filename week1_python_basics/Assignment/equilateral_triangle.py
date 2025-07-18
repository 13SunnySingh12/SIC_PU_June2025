#e#Print the Equilateral Triangle by accepting number of lines

def equilateral_triangle(lines):
    if lines < 2:
        print("Invalid Input. Please enter at least 2 lines.")
    else:
        for i in range(1, lines + 1):
            print(' ' * (2 * lines - i) + '* ' * i)

line = int(input("Enter the number of lines for the equilateral triangle: "))
equilateral_triangle(line)

