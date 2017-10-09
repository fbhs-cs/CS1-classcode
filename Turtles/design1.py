from turtle import *


def draw_hex(size):
    for i in range(6):
        fd(size)
        rt(60)

def draw_figure():
    for i in range(120):
        draw_hex(200)
        rt(10.5)
        
def main():
    speed(0) # sets the speed of the drawing to 0, which is fastest
    color('white') # sets the color of the turtle to white
    bgcolor('black') #sets the background color to black
    pu() # short for penup()
    pd() # short for pendown()
    draw_figure()
    
main()