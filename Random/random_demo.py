import random

rps = random.random()
if rps < 0.33333:  #will be true 1/3 of the time
    print("ROCK")
elif rps < 0.66667:
    print("PAPER")
else:
    print("SCISSORS")


#pick for random integers, each 1-10
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
d = random.randint(1,10)
print(" 1-10:\t{}\t{}\t{}\t{}".format(a,b,c,d))

#pick for random integers, each 1-10
a = random.randint(10,20)
b = random.randint(10,20)
c = random.randint(10,20)
d = random.randint(10,20)
print("10-20:\t{}\t{}\t{}\t{}".format(a,b,c,d))


#TODO choose random numbers
#between 70 and 100
#and print them out
