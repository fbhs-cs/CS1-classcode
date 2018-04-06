with open("words.txt") as file:
        wordlist = file.read().splitlines()
import random
def rand_word():
    with open('words.txt') as file:
        wordlist = file.read().splitlines()
    word = ''
    
    while len(word) < 10 or len(word) > 15:
            word = random.choice(wordlist)
            
    return word

def print_man(numguess):
    if numguess == 0:
        print(' +--+')
        print('    |')
        print('    |')
        print('    |')
        print('    |')
        print('______')
    elif numguess == 1:
        print(' +--+')
        print(' O  |')
        print('    |')
        print('    |')
        print('    |')
        print('______')
    elif numguess == 2:
        print(' +--+')
        print(' O  |')
        print(' |  |')
        print('    |')
        print('    |')
        print('______')
    elif numguess == 3:
        print(' +--+')
        print(' O  |')
        print('\|  |')
        print('    |')
        print('    |')
        print('______')
    elif numguess == 4:
        print(' +--+')
        print(' O  |')
        print('\|/ |')
        print('    |')
        print('    |')
        print('______')
    elif numguess == 5:
        print(' +--+')
        print(' O  |')
        print('\|/ |')
        print(' |  |')
        print('    |')
        print('______')
    elif numguess == 6:
        print(' +--+')
        print(' O  |')
        print('\|/ |')
        print(' |  |')
        print('  \ |')
        print('______')
    elif numguess == 7:
        print(' +--+')
        print(' O  |')
        print('\|/ |')
        print(' |  |')
        print('/ \ |')
        print('______')






