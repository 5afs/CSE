import random
money = 15
broke = False
round = 1

print("Welcome to Lucky 7s!")

while money > 0:
    d6_1 = random.randint(1, 6)
    d6_2 = random.randint(1, 6)
    if d6_1 + d6_2 == 7:
        money = money + 5
        round += 1
    elif d6_1 + d6_2 != 7:
        money = money - 1
        round += 1

if money == 0:
    broke = True
    print("You're broke! You lasted for %d rounds." % round)
