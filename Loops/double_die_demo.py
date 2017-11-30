from random import randint

def roll():
    die1 = randint(1,6)
    die2 = randint(1,6)
    print('Roll #1:',die1)
    print('Roll #2:',die2)
    print('The total is {}!'.format(die1+die2))
    if die1 == die2:
        return True
    return False

while not roll():
    print()