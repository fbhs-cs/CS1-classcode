def is_prime(n):
    '''returns True if n is prime
       and False otherwise
    '''
    upper_bound = int(n ** 0.5)+1
    for i in range(2,upper_bound):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num