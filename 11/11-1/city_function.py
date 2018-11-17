
def country_city_total_information(country, city, population=''):
    if population:
        description = country + ', ' + city + ' - ' + population
    else:
        description = country + ', ' + city
    return description.title()
