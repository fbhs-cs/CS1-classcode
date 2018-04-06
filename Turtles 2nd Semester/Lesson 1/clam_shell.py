from turtle import *

terry = Turtle()
terry.hideturtle()
terry.speed(0)

circle_size = 6
for i in range(9):
    terry.circle(circle_size + circle_size * i)

