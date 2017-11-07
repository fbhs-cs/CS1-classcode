import math

def afunc(val):
    for i in range(val):
        print(i)

def area(radius):
    '''returns the area of a circle with radius
    '''
    a = math.pi * radius ** 2
    return a  

def surf_area(radius):
    sa = 4 * area(radius)
    return sa

def absolute_value(x):
    '''returns the absolute value of x
    '''
    if x < 0:
        return -x
    else:
        return x
   
    

def compare(x, y):
    '''returns 1 if x is greater than  y
       returns 0 if x is equal to y
       returns -1 if x is less than y
    '''
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    else:
        print('THIS SHOULDNT HAPPEN')


                   


