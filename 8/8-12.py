
def sandwich_order(*adds):
    print('sandwich with : ', end='')
    print(*adds, sep=', ', end='')
    print('.')


sandwich_order('ham', 'cheese', 'bacon', 'mushrooms')