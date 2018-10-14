dictionary = {
    'nil' : 'egypt',
    'volga' : 'russia',
    'temza' : 'france'
    }

for rivers, countries in dictionary.items():
    print('The ', rivers.title(), ' runs through ', countries.title())

print('\nRivers:')
for rivers in dictionary.keys():
    print('  ' + rivers.title())
print('\nCountries:')
for countries in dictionary.values():
    print('  ' + countries.title())