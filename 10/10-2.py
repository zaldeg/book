with open('files/learning_python.txt') as file_object:
    for line in file_object.readlines():
        print(line.strip().replace('Python', 'C'))