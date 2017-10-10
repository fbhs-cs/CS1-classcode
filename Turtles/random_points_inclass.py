from turtle import *
from random import randint



# We will write the code for this program together in class
def rand_color():
    colormode(255)   # necessary to use rgb colors
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color(r,g,b)

def draw_dots(num_dots):
    for i in range(num_dots):
        pu()
        randx = randint(-375,375)
        randy = randint(-320,320)
        goto(randx,randy)
        rand_color()
        dot(randint(3,25))
        ht()

def main():
    bgcolor('black')
    color('white')
    title('purdy dots!')
    speed(0)
    draw_dots(100)
    
main()