# Stripping every non-letter from a string with re.sub and a negated class.

import re

data = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]

# Remove all non-alphabetic characters
cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]', '', s), data))
print(cleaned) 
                       