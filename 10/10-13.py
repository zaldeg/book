import json


def get_stored_username():
    filename = 'files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('Enter your name \n')
    filename = 'files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print('Welcome back ' + username + '!')
    else:
        username = get_new_username()
        print('We will remember you ' + username + '!')


def check_username():
    username = get_stored_username()
    if username:
        c_name = input('Hello are you ' + username + '?')
        if c_name == username:
            greet_user()
        else:
            get_new_username()
    else:
        get_new_username()


check_username()