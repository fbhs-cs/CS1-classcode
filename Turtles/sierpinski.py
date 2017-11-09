import random
from turtle import *


def draw_sierpinski(length, depth):
    
    if depth == 0:
        color('blue')
        
        begin_fill()
        for i in range(3):
            fd(length)
            left(120)
        end_fill()
    else:
        draw_sierpinski(length/2, depth - 1)
        fd(length/2)
        draw_sierpinski(length/2, depth - 1)
        bk(length/2)
        left(60)
        fd(length/2)
        right(60)
        draw_sierpinski(length/2, depth - 1)
        left(60)
        bk(length/2)
        right(60)

def main():
    title("Sierpinski's Triangle")
    speed(0)
    pu()
    setpos(-150,0)
    pd()
    draw_sierpinski(300,4)
    
main()
