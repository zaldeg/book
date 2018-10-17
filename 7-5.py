# cost of ticket
while True:
    age = int(input('enter your age:\n\t'))
    if 0 < age < 3:
        print("\tIt's free")
    elif 3 <= age <= 12:
        print("\tIt's 10$")
    elif 13 <= age <= 1000:
        print("\tIt's 15$")