class SecretWord:
    def __init__(self, secret):
        self.secret = list(secret.lower())
        self.masked = ['*'] * len(self.secret)
        
    def __str__(self):
        return "".join(self.masked)
    
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
    

    

