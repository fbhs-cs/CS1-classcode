with open("words.txt") as file:
    wordlist=file.read().splitlines()
    
##for word in wordlist:
##    if len(word)== 12:
##        print(word)

    
def longest():
    
    for word in wordlist:
        if len(word)>=21:
            print(word)
        


def has_at_least(n):
    words=0
    for word in wordlist:
        if len(word) >=n:
            words+=1
    return words
    



def percent_with_e(words):
    count=0
    for word in words:
        if 'e' in word:
            count+=1
    print("{:.2f}% of the words have an 'e'".format(count/len(words)*100))



def avoids(words,string):
    count=0
    string=list(string)
    for i in words:
        for x in string:
            if x in i:
                break
        else:
            count+=1
    print("{:.2f}% of the words do not use {}.".format(count/len(words)*100,", ".join(string)))
                     



def uses_only(words,string):
    for word in words:
        for letter in word:
            if letter not in string:
                break
        else:
            print(word)     
        


def num_abecedarian(words):
	count=0
	for word in words:
    		if is_abecedarian(word) == True:
        		count+=1
	print(count)
	
def is_abecedarian(word):
	for i in range(len(word)-1):
    		if word[i]>word[i+1]:
##        		print(word)
        		return False
	return True
 	
num_abecedarian(wordlist)

        
    
    
    


