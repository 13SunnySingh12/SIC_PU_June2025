# Pulling every run of digits out of each string with re.findall.

import re

data = ["abc123", "hello2024", "no digits", "zip007"]

# Extract digits using regex and lambda
digits = list(map(lambda s: re.findall(r'\d+', s), data))
print(digits)  
