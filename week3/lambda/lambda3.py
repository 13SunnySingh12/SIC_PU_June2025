def power_factory(exponent):
    return lambda base: base ** exponent

square = power_factory(2)
cube = power_factory(3)

print(f"5 squared is: {square(5)}")
print(f"5 cubed is: {cube(5)}")
