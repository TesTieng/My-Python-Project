# Python program to draw

from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(140, 'magenta')
    back(100)
    right(120)
    forward(100)
    dot(140, 'sky blue')
    back(100)
    right(120)
    forward(100)
    dot(140, 'yellow green')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 30)
def flick():
    state['turn']+=75

setup(420, 420, 370, 0)
bgcolor("black")
hideturtle()
tracer(False)
width(50)
color('orange')
onkey(flick, 'space')
listen()
animate()
done()