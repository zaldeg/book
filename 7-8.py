sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'meat sandwich', 'ham sandwich', 'cheese sandwich']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ', current_sandwich)
    finished_sandwich.append(current_sandwich)
print('\n\t\tList of sandwiches i made:')
while finished_sandwich:
    print(finished_sandwich.pop())