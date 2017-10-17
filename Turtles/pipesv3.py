from turtle import *
from random import randint, choice

def rand_color():
    colormode(255)   # necessary to use rgb colors
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color(r,g,b)

def draw_pipes():
    speed(0)
    directions = [0,90,180,270]
    width(5)
    while True:
        if xcor() >= 375: 
            pu()
            goto(-375,ycor())
            pd()
        elif xcor() <= -375:
            pu()
            goto(375,ycor())
            pd()
        elif ycor() >= 320: 
            pu()
            goto(xcor(),-320)
            pd()
        elif ycor() <= -320:
            pu()
            goto(xcor(),320)
            pd()
            
        seth(choice(directions))
        rand_color()
        fd(randint(25,75))

def main():
    speed(0)
    bgcolor('black')
    draw_pipes()
    
main()