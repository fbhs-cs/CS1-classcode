def count_evens(tup):
    num_evens = 0
    for i in tup:
        if i % 2 == 0:
            num_evens += 1
    return num_evens

def count_odds(tup):
    num_odds = 0
    for i in tup:
        if i % 2 != 0:
            num_odds += 1
    return num_odds

def count_primes(tup):
    primes = 0
    for i in tup:
        factors = 0
        if i > 2:
            for j in range(2, i):
                if i % j == 0:
                    factors += 1
			    break
        if factors == 0:
            primes += 1
    return primes
            
def main():
    tester_tup = (1, 2, 3, 4, 5, 6, 7)
    print(count_evens(tester_tup))
    print(count_odds(tester_tup))
    print(count_primes(tester_tup))

if __name__ == '__main__':
    main()

