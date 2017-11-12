from turtle import *

def func1(x):
    for i in range(4):
        forward(x)
        lt(90)
        
def func2(x):
    for i in range(x):
        forward(60)
        lt(60)
    
def rectangle(x,y):
    forward(x)
    lt(90)
    forward(y)
    lt(90)
    forward(x)
    lt(90)
    forward(y)
    lt(90)


def func3(x, y):
    if x % y == 0:
        print('{} is divisible by {}'.format(x,y))
    if x / y == 2:
        print('{} is twice as large as {}'.format(x,y))
    if x - y == 0:
        print('{} is equal to {}'.format(x,y))
    
        
def func4(x):
    for i in range(1,x):
        if x % i == 0:
            print(i)
        elif i < x:
            print(x)
        else:
            print(0)


def func5(x,y,z):
    if x > y:
        if y > z:
            print('{} > {}'.format(x,z))
        else:
            print('{} < {}'.format(x,z))
    elif y > x:
        if x > z:
            print('{} > {}'.format(y,z))
        else:
            print('{} < {}'.format(y,z))
    else:
        print('{} > {}'.format(z,x))

def func6(x):
    if x > 5:
        return x
    elif x < 5:
        return 5
    

def rec_func1(x):
    if x == 0:
        return 0
    else:
        return x + rec_func1(x-1)
    

def rec_func2(x,n):
    if n == 0:
        return 1
    return x * rec_func2(x,n-1)


from random import randint
x = randint(1,10)
y = randint(1,10)
z = randint(1,5)



num = input('Enter a value: ')
if num > 10:
    print('Too big!')
elif num < 10:
    print('Too small!')
else:
    print('Just right!')