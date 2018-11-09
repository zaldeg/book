file = 'files/' + input() + '.txt'
try:
    with open(file) as file_object:
        nicknames = file_object.read()
except FileNotFoundError:
    print("File " + file + " was not found")
else:
    print(nicknames)