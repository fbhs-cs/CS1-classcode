from turtle import *

from random import randint #import randint function from random module

def rand_color():
    colormode(255)       # necessary to use rgb colors
    r = randint(0,255)   # makes variables r, g, and b with
    g = randint(0,255)   # values between 0 and 255.
    b = randint(0,255)   # this color will change every time
                         # the loops run
                         
    color(r,g,b)         # changes the color of the turtle to
                         # the rgb values made above 

def draw_figure(size):
    for i in range (400):
        rand_color()               
        fd(size + i)
        rt(90.911)
    
def main():
    speed(0)
    colormode(255)   #necessary to use rgb colors below
    bgcolor('black')
    pu()
    pd()
    draw_figure(100)

main()