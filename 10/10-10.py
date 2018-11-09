file = 'files/' + input('Enter book name') + '.txt'
print(file)

try:
    with open(file) as file_object:
        words = file_object.read().lower().split()
except FileNotFoundError:
    print('Next time give me file name')
else:
    print(words.count('and'))