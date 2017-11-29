def collatz(n):
    count = 0
    print('Starting with',n,'...')
    while n != 1:
        print(n,end = ' ')
        if n % 2 == 0:  # n is even
            n = n // 2
        elif n %2 == 1: # n is odd
            n = 3 * n + 1
    print(n)          
            
def main():
    num = int(input('What is the starting value?\n> '))
    collatz(num)    
    
# Tell Python to run main if the program is being run (not imported)    
if __name__ == '__main__':
    main()