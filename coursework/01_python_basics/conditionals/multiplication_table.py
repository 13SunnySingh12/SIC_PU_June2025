#Accept a number from thr user and print it's math table.

input_number = int(input("Enter a number to print its Math table: "))

for i in range(1,11):  
    print('%2d * %2d = %3d' % (input_number, i, input_number * i))
