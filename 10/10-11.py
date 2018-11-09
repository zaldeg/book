import json

favorite_number = int(input('Enter your favorite number\n'))

filename = 'files/favorite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
