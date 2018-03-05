def even_count(tup):
    evens = 0
    for i in range(len(tup)):
        num = tup[i]
        if num % 2 == 0:
            evens += 1
    return evens

def odd_count(tup):
    odds = 0
    for i in range(len(tup)):
        num = tup[i]
        if num % 2 != 0:
            odds += 1
    return odds

def prime_count(tup):
    primes = 0
    for i in range(len(tup)):
            num = tup[i]
            if num > 1:
                for i in range(2,num-1):
                    if (num % i) == 0:
                        break
                    else:
                        primes += 1
                        break
    return primes

def main():
    my_tuple = (2, 9, 4, 6, 3, 7, 8, 15,13)
    print(even_count(my_tuple)) #4
    print(odd_count(my_tuple)) #4
    print(prime_count(my_tuple)) #3
    
if __name__ == "__main__":
    main()
