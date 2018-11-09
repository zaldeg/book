import json


def ask_number():
    with open(filename, 'w') as f_obj:
        f_number = input('Hello enter your favorite number pls: \n')
        json.dump(f_number, f_obj)


def greeting():
    try:
        with open(filename) as f_obj:
            f_number = json.load(f_obj)
            print('Hello your favorite number is ', f_number)
    except FileNotFoundError:
        ask_number()


filename = 'files/favorite_number2.json'
greeting()
