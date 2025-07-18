import numpy as np

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
days = {1: 'mon', 2: 'tues', 3: 'wed', 4: 'thurs', 5: 'fri', 6: 'sat', 7: 'sun'}

max_index = np.argmax(week_spendings)
max_spending = week_spendings[max_index]

print(max_spending, days[max_index + 1])
