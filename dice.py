import random
our_chance = 95
win = 155.5263
times = int(input('times'))
bet_size = 150
for j in range(50):
    summ = 0
    summ2 = 0
    for i in range(times):
        chance = random.randrange(1,101,1)
        if chance <= our_chance:
            summ += win
        summ2 += bet_size
    '''print(summ)
    print(summ2)
    print(summ2/summ)'''
 #   ref = summ2 * 0.002 + summ2 * 0.0162
    summ3 = summ #+ ref
    print(int((summ3 - summ2)), '\t', '''ref''', '\t', ((summ3 - summ2)/summ2)*100)