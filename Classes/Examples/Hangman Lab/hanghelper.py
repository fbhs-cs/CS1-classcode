<<<<<<< HEAD
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






=======
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
    
>>>>>>> dc81307e9734aba5a14cebe6f87ecbca91c15b80
