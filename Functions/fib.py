from turtle import *
from random import *


def star():
    color('white')
    for i in range(80):
        pu()
        x = randint(-320,320)
        y = randint(40,300)
        setpos(x,y)
        dot(randint(3,6))
 
def snowman():
    pu()
    setpos(40,-60)
    color('grey')
    begin_fill()
    circle(40)
    setpos(40,-120)
    circle(40)
    setpos(40,-160)
    circle(40)
    end_fill()
    carrot()
    setpos(43,5)
    color('black')
    dot(7)
    pu()
    setpos(38,5)
    
    
    
    
def carrot():
    setpos(40,0)
    color('orange')
    begin_fill()
    rt(90)
    fd(30)
    rt(120)
    fd(30)
    rt(120)
    fd(30)
    end_fill()
    
def bow(x,y):
    setpos(x,y)
    seth(0)
    color('red')
    begin_fill()
    for i in range(4):
        fd(20)
        rt(90)
        end_fill()




def present():
    pu()
    setpos(-90,-40)
    color('yellow')
    begin_fill()
    seth(0)
    fd(80)
    rt(90)
    fd(40)
    rt(90)
    fd(80)
    rt(90)
    fd(40)
    end_fill()
    

    
    





def ground():
    color('white')
    pu()
    begin_fill()
    setpos(-380,0)
    pd()
    setpos(375,0)
    setpos(375,-350)
    setpos(-380,-350)
    setpos(-380,0)
    end_fill()
    pu()
    

    
def christmas_wreath(x,y):
    pu()
    setpos(x,y)
    pd()
    color('green')
    begin_fill()
    triangle()
    setpos(x,y-12)
    triangle()
    setpos(x,y-24)
    triangle()
    setpos(x,y-30)
    triangle()
    setpos(x,y-47)
    triangle()
    setpos(x,y-54)
    triangle()
    setpos(x+2,y-47)
    triangle()
    end_fill()
    pu()
    bow(-170,0)
    
    
def triangle():
    settiltangle(70)
    rt(60)
    fd(80)
    rt(120)
    fd(80)
    rt(120)
    fd(80)
    




def main():
    speed(0)
    bgcolor('black')
    ground()
    pu()
    star()
    snowman()
    present()
    christmas_wreath(-170,20)
    
main()