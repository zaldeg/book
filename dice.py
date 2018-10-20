import random
our_chance = 95
win = 103.6842
times = int(input('times'))
bet_size = 100
l = list()
summroi = 0
for j in range(10000):
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
    ref = summ2 * 0.002 + summ2 * 0.0137 + summ2 * 0.0006
    summ3 = summ + ref
    l.append(int(summ3 - summ2))
    print(int((summ3 - summ2)), '\t', ref, '\t', ((summ3 - summ2)/summ2)*100)
    summroi += ((summ3 - summ2)/summ2)*100
print(l)
a = sorted(l)
print(a)
count = 5
while a:
    summ10 = 0
    for i in range(1000):
        summ10 += a.pop()
    print(summ10 / 1000,  '  :', count,'%')
    count += 10
print(summroi / 10000)