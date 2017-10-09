from turtle import *


def color_square(side_length,c_out,c_fill,x,y):
    color(c_out,c_fill)
    penup()
    setpos(x,y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(side_length)
        right(90)
    end_fill()
    color('black')
speed(1)
color('red','blue')
begin_fill()
for i in range(12):
    circle(50,90)
    right(120)
end_fill()

#color_square(300,'red','blue',-150,150)
#color_square(200,'green','orange',-100,100)
#color_square(100,'yellow','sky blue',-50,50)


