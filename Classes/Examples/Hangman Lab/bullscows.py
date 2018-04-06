from secretword import SecretWord
import random

class BullsAndCows:
    def __init__(self):
        wordlist = ['apple','basketball','computer',
                    'guitar','television','bookcase']
        self.secret = SecretWord(random.choice(wordlist))
    
    def play(self):
        pass
        # Write code here to play the game.
        # 1. Display a welcome message
        # 2. Display the masked secret word
        # 3. Ask the user for a guess
        # 4. Display the appropriate output based on
        #    the rules of Bulls and Cows
        # 5. Repeat 3 and 4 until the player gets the word

def main():
    game = BullsAndCows()
    game.play()
    
    
if __name__ == "__main__":
    main()