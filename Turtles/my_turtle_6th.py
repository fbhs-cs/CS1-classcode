from turtle import *


def color_square(side_length,x,y,b_col,f_col):
    penup()
    setpos(x,y)
    pendown()
    color(b_col,f_col)
    begin_fill()
    for i in range(4):
        forward(side_length)
        right(90)
    end_fill()
    color('black')
    
#color_square(300,75,0,'blue','orange')
#color_square(200,-100,100,'red','pink')
#color_square(100,-50,50,'green','turquoise')

color('green')
begin_fill()
seth(90)
for i in range(8):
    circle(50)
    right(45)
end_fill()

