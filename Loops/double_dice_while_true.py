'''
keeps rolling a pair of dice, displaying their total
until doubles are rolled.
'''
from random import randint
while True:
    d1 = randint(1,6)
    d2 = randint(1,6)
    print('Roll #1:',d1)
    print('Roll #2:',d2)
    print('The total is {}!'.format(d1+d2))
    print()
    if d1 == d2:
        break
    
    