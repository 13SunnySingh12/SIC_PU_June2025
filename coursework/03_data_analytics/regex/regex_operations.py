# A tour of the regex operations used most often: findall to extract digits and
# non-digits, sub to strip or collapse characters, sub with a function to
# capitalise a leading vowel, and search with a capture group to pull the
# domain out of an email address.

import re

data = ["hi123  ", "hello123  ", "hum  ", "dig345  "]

only_digits = list(map(lambda s: re.findall(r'\d+', s), data))
print(only_digits)

only_strings_split = list(map(lambda s: re.findall(r'\D+', s), data))
print(only_strings_split)

digits_clean = list(map(lambda s: re.sub(r'\D+', '', s), data))
print(digits_clean)

vowel_capitalized = list(map(lambda w: re.sub(r'^[aeiouAEIOU]', lambda m: m.group(0).upper(), w), data))
print(vowel_capitalized)

single_spaced = list(map(lambda s: re.sub(r'\s+', ' ', s), data))
print(single_spaced)

emails = ["a@gmail.com", "b@yahoo.com"]
domains = list(map(lambda s: re.search(r'@(\w+)\.', s).group(1), emails))
print(domains)
