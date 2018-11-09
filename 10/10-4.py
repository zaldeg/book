"""creating guest book with quit 'q'"""

with open('files/guest_book.txt', 'w') as file_object:
    while True:
        new_guest_name = input("Hello what's your name? if you write 'q' the programme is end\n")
        if new_guest_name == 'q':
            break
        file_object.write(new_guest_name + '\n')
