import random

def rand_word():
    with open('words.txt') as file:
        wordlist = file.read().splitlines()
    
    word = ''
    while len(word) < 10 or len(word) > 15:
        word = random.choice(wordlist)
    
    return word


def print_man(n):
    if n == 0:
        print(' +--+  ')
        print('    |  ')
        print('    |  ')
        print('    |  ')
        print('    |  ')
        print('-------')
    elif n == 1:
        print(' +--+  ')
        print(' O  |  ')
        print('    |  ')
        print('    |  ')
        print('    |  ')
        print('-------')
        
        
    elif n == 2:
        print(' +--+  ')
        print(' O  |  ')
        print(' |  |  ')
        print('    |  ')
        print('    |  ')
        print('-------')
        
        
    elif n == 3:
        print(' +--+  ')
        print(' O  |  ')
        print('\|  |  ')
        print('    |  ')
        print('    |  ')
        print('-------')
        
    elif n == 4:
        print(' +--+  ')
        print(' O  |  ')
        print('\|/ |  ')
        print('    |  ')
        print('    |  ')
        print('-------')
        
    elif n == 5:
        print(' +--+  ')
        print(' O  |  ')
        print('\|/ |  ')
        print(' |  |  ')
        print('    |  ')
        print('-------')
        
    elif n == 6:
        print(' +--+  ')
        print(' O  |  ')
        print('\|/ |  ')
        print(' |  |  ')
        print('/   |  ')
        print('-------')
        
    elif n == 7:
        print(' +--+  ')
        print(' O  |  ')
        print('\|/ |  ')
        print(' |  |  ')
        print('/ \ |  ')
        print('-------')
    