from secretword import *

try:
    print("Testing init")
    sw = SecretWord("testing")
except Exception as e:
    print("Cannot initialize SecretWord:",e)

try:
    print("Testing __str__...should print ******")
    print(sw)
except Exception as e:
    print("Cannot print secretword:",e)
    
try:
    print("Testing guess_word")
    print(sw.guess_word("tasting"))
    print(sw.guess_word("tipping"))
    print(sw.guess_word("stinget"))
    print(sw.guess_word("toolong"))
    print(sw.guess_word("tooshort"))

except Exception as e:
    print('guess_word not working:',e)
    
try:
    print("unmasking letters...")
    print("s")
    sw.unmask_letter("s")
    print(sw)
    print("t")
    sw.unmask_letter("t")
    print(sw)
    print("x")
    sw.unmask_letter('x')
    print(sw)
except Exception as e:
    print('unmask_letter not working:',e)