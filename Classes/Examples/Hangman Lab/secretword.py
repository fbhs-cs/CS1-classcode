class SecretWord:
    def __init__(self, secret):
<<<<<<< HEAD
        self.secret = list(secret.lower())
        self.masked = ['*'] * len(self.secret)
=======
        self.secret = list(secret)
        self.masked = ['*'] * len(secret)
>>>>>>> dc81307e9734aba5a14cebe6f87ecbca91c15b80
        
    def __str__(self):
        return "".join(self.masked)
    
<<<<<<< HEAD
    def guess_word(self,guess):
        guess = guess.lower()
        if len(guess) != len(self.secret):
            return "Length must be {}.".format(len(self.secret))
        unmasked = self.masked[:]
        secret_copy = self.secret[:]
        for i in range(len(self.secret)):
            if self.secret[i] == guess[i]:
                unmasked = guess[i]
                secret_copy[i] = '*'
            elif guess[i] in secret_copy:
                unmasked[i] = '+'
                secret_copy[secret_copy.index(guess[i])] = '*'
        return ''.join(unmasked)
        

def main():
    my_word = SecretWord("hornets")
    print(my_word)
    
if __name__ == "__main__":
    main()
    

    

=======
    def get_word(self):
        return "".join(self.secret)
    
    def guess_word(self,guess):
        guess = guess.lower()
        if len(guess) != len(self.secret):
            return "Bad guess: length must be {}.".format(len(self.secret))
        
        unmasked = self.masked[:]
        secret_copy = self.secret[:]

        for i in range(len(self.secret)):
            if self.secret[i] == guess[i]:
                unmasked[i] = guess[i]
                secret_copy[i] = '*'
        
        for i in range(len(self.secret)):
            if guess[i] in secret_copy and unmasked[i] == '*':
                unmasked[i] = "+"
                secret_copy[secret_copy.index(guess[i])] = '*'
        
        return ''.join(unmasked)
    
    def unmask_letter(self,letter):
        found = False
        for i in range(len(self.secret)):
            if self.secret[i] == letter:
                self.masked[i] = letter
                found = True
        return found
            
    
def main():
    my_word = SecretWord("hornets")
    print(my_word)
    my_word.guess_word('hotdogs')
    
    
if __name__ == "__main__":
    main()
>>>>>>> dc81307e9734aba5a14cebe6f87ecbca91c15b80
