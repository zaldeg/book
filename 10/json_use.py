import json

numbers = [1, 3, 4, 5, 6, 7, 7]

with open('numbers.json', 'w') as f_obj:
    json.dump(numbers, f_obj)
