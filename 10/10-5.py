"""input reason to programming and write into file 'programming_reasons.txt'"""

with open('files/programming_reasons.txt', 'w') as file_object:
    while True:
        reason = input('Enter a reason to programme, if u write "q" programme ends\n')
        if reason == 'q':
            break
        file_object.write(reason + '\n')
