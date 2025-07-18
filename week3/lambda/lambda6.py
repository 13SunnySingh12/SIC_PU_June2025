people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 25}
]

# Sort by age, then by name
people.sort(key=lambda p: (p['age'], p['name']))
print(people)
