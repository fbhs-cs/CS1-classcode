from random import randint

die1 = 0
die2 = 1
while die1 != die2:
    die1 = randint(1,6)
    die2 = randint(1,6)
    print('Roll #1:',die1)
    print('Roll #2:',die2)
    print('The total is {}!'.format(die1+die2))
    print()
