file = 'files/' + input() + '.txt'
try:
    with open(file) as file_object:
        nicknames = file_object.read()
except FileNotFoundError:
    pass
else:
    print(nicknames)