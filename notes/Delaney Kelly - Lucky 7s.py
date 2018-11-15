import random
money = 15
round = 1
richest_round = round
most_money = money
broke = False
won = False

while money > 0:
    d6_1 = random.randint(1, 6)
    d6_2 = random.randint(1, 6)
    if d6_1 + d6_2 == 7:
        money = money + 4
        round += 1
        won = True
        richest_round = round + 1
        if money > most_money:
            most_money = money
    elif d6_1 + d6_2 != 7:
        money = money - 1
        round += 1
        won = False

if money == 0:
    broke = True
    print("You're broke! You lasted for %d rounds." % round)
    print("The most money you've had is $%d in round %d" % (most_money, richest_round))
