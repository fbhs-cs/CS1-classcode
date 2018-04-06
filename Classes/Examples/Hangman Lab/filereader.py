with open("words.txt") as file:
    wordlist = file.read().splitlines()
##for word in wordlist:
##    if len(word) == 12:
##        print(word)

def longest():
    for word in wordlist:
        if len(word) > 20:
            print(word)

def has_at_least(n):
    for word in wordlist:
        if len(word) == n:
            print(word)

def percent_with_e(words):
    count = 0
    for word in words:
        if 'e' in word:
            count += 1
    print("{:.2f}% of the words have an \'e'".format(count/len(words)*100))
    
def words_with_no_e():
    for word in wordlist:
        if 'e' not in word:
            print(word)
            
def avoids(words, avo):
    count = 0
    for word in words:
        for letter in avo:
            if letter in word:
                count += 1
                break
    print("{:.2f}% of words don't have letters in '{}'".format(100 - count/len(words)*100, " ,".join(avo)))

def uses_only(words,letters):
    for word in words:
        for letter in word:
            if letter not in letters:
                break
        else:
            print(word)
            
def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def num_abecedarian(words):
    count = 0
    for word in words:
        if is_abecedarian(word):
            count += 1
    print(count)
    


