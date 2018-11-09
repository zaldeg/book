import json

filename = 'files/favorite_number.json'
with open(filename) as f_obj:
    favorite_number = json.load(f_obj)

print('Hello! your favorite number is ' + str(favorite_number))