def count_prime_digits_in_number(number):
    prime_digit_count = 0
    for digit_char in str(number):
        digit = int(digit_char)
        if digit < 2:
            print(digit,"is not prime.")
            continue
        for i in range(2, int(digit ** 0.5) + 1):
            if digit % i == 0:
                break
        else:
            prime_digit_count += 1
    return prime_digit_count

num = int(input("Enter a number: "))
print("Number of prime digits:", count_prime_digits_in_number(num))
