points = [
    {'x': 1, 'y': 2},
    {'x': 3, 'y': 4},
    {'x': 0, 'y': 0}
]

# Sort by distance from origin
points.sort(key=lambda p: (p['x']**2 + p['y']**2)**0.5)
print(points)
