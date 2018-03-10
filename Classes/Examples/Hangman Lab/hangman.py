from hanghelper import *
from secretword import *

class Hangman:
    
    def __init__(self):
        self.secret = SecretWord(rand_word())
        self.guesses = []
        self.guesses_left = 7
        
    def show(self):
        print(self.secret)
        print_man(7 - self.guesses_left)
    
    def check_guess(self,guess):
        if len(guess) > 1:
            print('No cheating!\n')
            return
        
        elif  'z' < guess.lower()  or guess.lower() < 'a':
            print("That is not a letter!\n")
            return
        
        elif guess.lower() in self.guesses:
            print("You already guessed '{}'\n".format(guess.lower()))
            return
        
        else:
            found = self.secret.unmask_letter(guess.lower())
            if not found:
                self.guesses_left -= 1
            self.guesses.append(guess.lower())
            
    
    def play(self):
        print('Try to guess the secret word...')
        print()
        while True:
            if self.guesses_left == 0:
                self.show()
                print("You're out of guesses!")
                print("The word was '{}'".format(self.secret.get_word()))
                return
            
            if str(self.secret).count('*') == 0:
                self.show()
                print('You got it! Great job!')
                return
            
            self.show()
            guess = input('Enter a letter: ').lower()
            print()
            self.check_guess(guess)


def main():
    print('Welcome to Hangman!')
    while True:
        game = Hangman()
        game.play()
        if input('Play again? (y/n)'.lower()) == 'n':
            break
    print('Thanks for playing!')

if __name__ == "__main__":
    main()
            
        