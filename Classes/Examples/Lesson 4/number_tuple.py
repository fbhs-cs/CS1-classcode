def even_count(tup):
    evens = 0
    # access each element in tup by index
    for i in range(len(tup)):
        if tup[i]%2==0:
            evens+=1
    return evens

def odd_count(tup):
    odds = 0
    # traverse the tuple with a for-each loop
    for i in tup:
        if i %2 != 0:
            odds+=1
    return odds


def prime_count(tup):
    primes = 0
    for num in tup:
        if num >1:
            for i in range(2,num):  #for-else loop - 
                if (num%i)==0:      #the else is executed only if the for loop
                    break           #finishes without interuption
            else:
                primes +=1
    return primes

def main():
    my_tuple = (2, 9, 4, 6, 3, 7, 8, 15, 21, 22, 23)
    print(even_count(my_tuple)) #4
    print(odd_count(my_tuple)) #4
    print(prime_count(my_tuple)) #3
if __name__ == "__main__":
    main()


