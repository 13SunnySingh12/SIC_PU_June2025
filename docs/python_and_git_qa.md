# Python and Git — written answers

Questions set during the Samsung Innovation Campus programme.

## Q1. What happens when we have 2 commits and we try to push?

**If the remote has no new changes** — the two local commits are pushed without
any issue.

**If the remote has new commits** — git rejects the push, because the remote
contains changes that are not present locally. To resolve it, run `git pull` to
fetch the remote changes and merge them with the local commits; after merging (or
resolving conflicts), the push succeeds.

**Force push** — `git push --force` overwrites the remote, but it is risky
because it can erase other people's work, so it is not recommended.

## Q2. Why are there no `++` and `--` operators in Python?

To keep the language simple and readable. Python uses `+= 1` and `-= 1` instead,
which are clearer and avoid the class of bugs that pre- and post-increment
ordering causes in other languages.

## Q3. How are floating-point numbers stored in memory?

Using the IEEE 754 standard, which splits the number into three parts:

1. **Sign bit** — whether the number is positive or negative.
2. **Exponent** — the range or scale of the number.
3. **Mantissa** — the actual value, i.e. the precision.

For a 32-bit float that is 1 bit of sign, 8 bits of exponent and 23 bits of
mantissa.

## Q4. Which module do these functions come from?

| Function | Module | Description |
|---|---|---|
| `range()` | builtins | Generates a sequence of numbers |
| `input()` | builtins | Gets input from the user |
| `print()` | builtins | Displays output to the console |
| `len()` | builtins | Returns the length of an object |
| `min()` | builtins | Returns the smallest item in an iterable |
| `max()` | builtins | Returns the largest item in an iterable |
| `sorted()` | builtins | Returns a sorted list from an iterable |

All seven are built-ins — they are always available with no import.
