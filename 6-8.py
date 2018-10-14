sharik = {
    'pet name' : 'sharik',
    'type of animal' : 'dog',
    'owner of the animal' : 'mr. derek'
    }
snegok = {
    'pet name' : 'snegok',
    'type of animal' : 'cat',
    'owner of the animal' : 'ms. kate'
    }
zorka = {
    'pet name' : 'zorka',
    'type of animal' : 'cow',
    'owner of the animal' : 'ms. banks'
    }
pets = [sharik, snegok, zorka]

for pet in pets:
    print(pet['pet name'].title(), ':')
    print('\tType of animal: ', pet['type of animal'])
    print('\tOwner of the animal: ', pet['owner of the animal'].title())