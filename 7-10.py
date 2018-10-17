places = dict()

print('For end of programme enter "q q"')

while True:
    name, place = input('Enter your name and favorite place:\n').split()
    if name == 'q':
        break
    places[name] = place

print('            List of names and places:')

for name, place in places.items():
    print('\t', name.title(), ' wants to go to the ', place.title())
