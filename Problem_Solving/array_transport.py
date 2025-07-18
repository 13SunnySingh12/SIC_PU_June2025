def get_frequency_map(numbers):
    frequency_map = {}
    for number in numbers:
        if number in frequency_map:
            frequency_map[number] += 1
        else:
            frequency_map[number] = 1
    return frequency_map

def get_missing_numbers(original_list, incomplete_list):
    original_freq = get_frequency_map(original_list)
    incomplete_freq = get_frequency_map(incomplete_list)

    missing_numbers = []
    for number in original_freq:
        original_count = original_freq[number]
        incomplete_count = incomplete_freq.get(number, 0)
        if original_count > incomplete_count:
            missing_numbers.append(number)

    return sorted(missing_numbers)

def main():
    original_list_size = int(input())
    incomplete_list = list(map(int, input().split()))
    full_list_size = int(input())
    original_list = list(map(int, input().split()))

    missing_numbers = get_missing_numbers(original_list, incomplete_list)
    print(' '.join(map(str, missing_numbers)))

if __name__ == "__main__":
    main()
