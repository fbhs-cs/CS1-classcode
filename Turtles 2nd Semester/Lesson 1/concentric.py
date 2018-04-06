from turtle import *


tina = Turtle()
tina.hideturtle()
radius = 40
for i in range(4):
    tina.circle(radius + radius * i)
    tina.penup()
    tina.goto(tina.xcor(),tina.ycor()-radius)
    tina.pendown()

