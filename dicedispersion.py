import random


def random_sum(rolls, win_chance, rounded_win_pot):
    """Return sum of montecarlo rolls"""
    winsum = 0
    for i in range(rolls):
        chance = random.randrange(1, 101, 1)
        if chance <= win_chance:
            winsum += rounded_win_pot
    return winsum


def number_of_simulations():
    """Return list of montecarlo simulations"""
    sim_list = []
    for i in range(simulations):
        sim_list.append(random_sum(rolls, win_chance, rounded_win_pot))
    return sim_list


def dispersion(sim_list, roi1=0):
    """describe dispersion"""
    sorted_sim_list = sorted(sim_list)
    step = len(sorted_sim_list) // 10
    range_percent = 95
    while sorted_sim_list:
        summ = 0
        for i in range(step):
            summ += sorted_sim_list.pop()
        with open('dice_result.txt', 'a') as file_object:
            avarege = (summ / step + (roi1 + rake) / 100 * rolls * buy_in)
            file_object.write(str(range_percent) + '%: ' + str(avarege - honest_roll_sum) + '\n')
#        print(str(range_percent) + '%: ' + str(summ / step + roi1 / 100 * rolls * buy_in - honest_roll_sum))
        range_percent -= 10


roi = 0.1
simulations = 10000
rolls = 50
buy_in = 1
win_chance = 49
rake = 1.5
win_pot = (1 + (100 - win_chance) / win_chance) * (1 - rake / 100)
rounded_win_pot = round(win_pot, 5)
win_sum_minus_rake = rolls * buy_in * (1 - rake / 100)
add_to_simulation = rake + roi
honest_roll_sum = rolls * buy_in

open('dice_result.txt', 'w').close()
while rolls < 15000:
    honest_roll_sum = rolls * buy_in
    with open('dice_result.txt', 'a') as file_object:
        file_object.write('rolls : ' + str(rolls) + '\n')
    dispersion(number_of_simulations(), roi)
    rolls *= 2

'''print(dispersion(number_of_simulations(), add_to_simulation))
print(honest_roll_sum)'''


