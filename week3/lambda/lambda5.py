products = [
    {'name': 'Keyboard', 'price': 75, 'in_stock': True},
    {'name': 'Monitor', 'price': 300, 'in_stock': False},
    {'name': 'Webcam', 'price': 100, 'in_stock': True}
]

min_price = 80

available_and_pricy = list(filter(lambda p: p['in_stock'] and p['price'] > min_price, products))
print(available_and_pricy)
