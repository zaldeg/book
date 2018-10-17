sandwich_orders = ['pastrami sandwich', 'tuna sandwich', 'pastrami sandwich', 'chicken sandwich', 'meat sandwich',
                   'ham sandwich', 'cheese sandwich', 'pastrami sandwich']
finished_sandwich = []
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ', current_sandwich)
    finished_sandwich.append(current_sandwich)
print('\n\t\tList of sandwiches i made:')
while finished_sandwich:
    print(finished_sandwich.pop())