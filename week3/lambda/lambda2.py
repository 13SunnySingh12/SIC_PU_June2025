from itertools import groupby

data = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'name': 'T-shirt', 'category': 'Apparel', 'price': 25},
    {'name': 'Mouse', 'category': 'Electronics', 'price': 50},
    {'name': 'Jeans', 'category': 'Apparel', 'price': 80}
]

data.sort(key=lambda x: x['category'])

grouped_data = {key: list(group) for key, group in groupby(data, key=lambda x: x['category'])}

for category, items in grouped_data.items():
    print(f"Category: {category}")
    for item in items:
        print(f"  - {item['name']}: ${item['price']}")
