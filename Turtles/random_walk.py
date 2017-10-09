from turtle import *
from random import randint

def rand_color():
    colormode(255)   # necessary to use rgb colors
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color(r,g,b)

def take_walk(num_steps, step_size):
    for i in range(num_steps):
        rand_ang = randint(0,360)  # get a random angle to turn
        seth(rand_ang)
        rand_color()
        fd(step_size)
        
def main():
    title('Random Walk')
    bgcolor('black')
    speed(0)
    take_walk(1000,20)
    
main()