"""print 3 different way"""

path = 'files/learning_python.txt'
with open(path) as file_object:
    content = file_object.read()
    print(content)

print('\n\n')

with open('files/learning_python.txt') as file_object1:
    file_represent = ''
    for line in file_object1.readlines():
        file_represent += line
    print(file_represent)

print('\n\n')

with open(path) as file_object2:
    for line in file_object2.readlines():
        print(line.strip())
