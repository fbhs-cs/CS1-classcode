def solve_doors():
    doors = 100 * [False]
    for step in range(1,len(doors)+1):
        for i in range(step-1,len(doors),step):
            doors[i] = not doors[i]
    for i in range(0,len(doors)):
        if doors[i]:
            print("Door #{} is open".format(i+1))
        

def sum_prod():
    nums = []
    sum = 0
    prod = 1
    while True:
        num = input("Enter a number (0 when finished):")
        if num == '0':
            break
        else:
            nums.append(num)
            sum += int(num)
            prod *= int(num)
    
    print(" + ".join(nums) + " = " + str(sum))
    print(" * ".join(nums) + " = " + str(prod))

sum_prod()

































