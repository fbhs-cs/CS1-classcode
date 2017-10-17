from turtle import *
from random import choice, randint
  
def draw_circles():
    ht()
    color_list = ['red','blue','green','orange','yellow','black','white']
    for i in range(1,21):
        pu()
        #color(choice(color_list))  #random from list
        color(color_list[i % 7])  #in the order of the list
        radius = 300 - 15*i
        begin_fill()
        goto(0,-radius)
        pd()
        circle(radius)
        end_fill()

    
def main():
    speed(0)
    draw_circles()
    
main()