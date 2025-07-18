from pprint import pprint

people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

print("Sort by age: ")
people.sort(key=lambda person: person['age'])
pprint(people)

print("Sort by name: ")
people.sort(key=lambda person: person['name'])
pprint(people)
