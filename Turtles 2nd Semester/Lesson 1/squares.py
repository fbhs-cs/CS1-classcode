from turtle import *


t = Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(-200,-200)
t.pendown()

for side_length in range(80,0,-10):
    for side in range(4):
        t.fd(side_length)
        t.lt(90)

    t.penup()
    t.goto(t.xcor()+side_length,t.ycor()+side_length)
    t.pendown()