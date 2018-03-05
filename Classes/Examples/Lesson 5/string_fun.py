def pig_latin(word):
    # return a new string that is word in pig latin.
    # move the first letter to the end of the word
    # then add the letters "ay" to the end
    # if the word is only one letter long, simply
    # return the word
    return word if len(word) == 1 else word[1:] + word[0] + 'ay'
    
    
def double_word(word):
    # return a new string that is word twice
    return 2*word

def backward(word):
    # return a new word that is word spelled backwards
    return word[::-1]

def delete(word, n):
    # return a new string with the nth letter removed 
    # from the word.
    # remember that strings are 0 indexed
    return word[:n] + word[n+1:]

def main():
    print(pig_latin("Monty"))            # ontyMay
    print(pig_latin("Python"))          # ythonPay
    print(pig_latin("z"))                # z
    print(double_word("Python"))        # PythonPython
    print(backward("Spam and Eggs"))    # sggE dna mapS
    print(delete("grail", 2))           # gril
    print(delete("grail", 4))           # grai
    print(delete("grail", 6))           # grail
    
if __name__ == "__main__":
    main()