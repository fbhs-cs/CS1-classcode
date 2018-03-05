from filereader import *
# get list of words from words.txt
with open("words.txt") as file:
    wordlist = file.read().splitlines()

score = 0

print("Testing longest()")
try:
    longest()
except:
    print("longest() failed.")
print()
score += float(input("Points earned: "))

print("Testing has_at_least(20)..should be 8")
try:
    print(has_at_least(20))
except:
    print("has_at_least(20) failed.")
print()
score += float(input("Points earned: "))



print("Testing percent_with_e(wordlist)...should be 66.93%")
try:
    percent_with_e(wordlist)
except:
    print("percent_with_e(wordlist) failed.")
print()
score += float(input("Points earned: "))

print("Trying avoids(wordlist,'aeiou')...should be 0.09%")
try:
    avoids(wordlist,'aeiou')
except:
    print("avoids(wordlist,'aeiou') failed.")
    
print("Trying avoids(wordlist,'pqxyz')...should be 65.72%")
try:
    avoids(wordlist,'pqxyz')
except:
    print("avoids(wordlist,'pqxyz') failed.")
    
print("Trying avoids(wordlist,'abcde')...should be 7.02%")
try:
    avoids(wordlist,'abcde')
except:
    print("avoids(wordlist,'abcde') failed.")
print()
score += float(input("Points earned: "))


print("Trying uses_only('be')")
try:
    uses_only(wordlist,'be')
except:
    "uses_only('be') failed."
score += float(input("Points earned: "))

print("Trying num_abecedarian(wordlist)...should be 596")
try:
    num_abecedarian(wordlist)
except:
    print("num_abecedarian failed")
score += float(input("Points earned: "))

print("Final Score:",(score+4))
    