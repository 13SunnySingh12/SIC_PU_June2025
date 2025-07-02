def frequency_of_elements(numbers):

     for number in set(numbers):
        count_numbers = numbers.count(number)
        print(number, "appears", count_numbers, "times")

input_numbers = list(map(int, input("Enter numbers: ").split()))
print(input_numbers)

frequency_of_elements(input_numbers)
