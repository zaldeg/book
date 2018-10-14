cities = {
    'S-Pb' : {
        'country' : 'russia',
        'population': '4.6m',
        'fact' : '300+ briges'
        },
    'Paris' : {
        'country' : 'france',
        'population': '3.5m',
        'fact' : 'Efeleva tower'
        },
    'London' : {
        'country' : 'england',
        'population': '7m',
        'fact' : 'queen'
    }
}

for city, characteristics in cities.items():
    print(city,':')
    print('\tCountry: ', characteristics['country'].title())
    print('\tPopulation: ', characteristics['population'])
    print('\tFact: ', characteristics['fact'])