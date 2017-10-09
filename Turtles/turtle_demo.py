from turtle import *

def color_square(side_length,x,y,c):
    color(c)
    penup()
    setpos(x,y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(side_length)
        right(90)
    end_fill()
    color('black')

def color_circle(radius, x, y, c_out, c_fill):
    color(c_out,c_fill)
    penup()
    setpos(x,y)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    color('black')

color_circle(150, -100, 0, 'sky blue', 'maroon')
##color_square(300,-150,150,'red')
##color_square(200,-150,150,'yellow')
