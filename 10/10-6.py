try:
    a = int(input('Input first number:\n'))
    b = int(input('Input second number:\n'))
except ValueError:
    print('one of inputs not a number')
else:
    print('Your answer:', a + b)