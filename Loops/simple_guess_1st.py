from random import randint

secret = randint(1,20) 
print('Guess a number between 1 and 20')
guess = int(input('> ')) 
while guess != secret:
    print('Nope, that was not it.')
    print()
    print('Guess a number between 1 and 20')
    guess = int(input('> '))      
print('You got it.')