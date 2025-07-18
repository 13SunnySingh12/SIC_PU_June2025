#Print the Right Angle Triangle by accepting number of lines

def right_angle_triangle(lines):
    if lines < 2:
        print("Invalid Input, enter number grater than 1.")
    else:     
        for i in range(1, lines + 1):
            print('* ' * i)

line = int(input("Enter the number of lines for the right angled triangle: : "))
right_angle_triangle(line)
