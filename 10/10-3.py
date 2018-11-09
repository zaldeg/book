guest_name = input('Hello , input you full name please:\n')

with open('files/guest.txt', 'w') as file_object:
    file_object.write(guest_name)
