# TODO 1: Create the Screen

from turtle import Screen, Turtle
from paddle1 import Paddles
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")



#TODO 2: Create the paddles
paddle1 = Paddles()

#paddle2 = Paddles()

#TODO 3: Make the paddles move
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

#screen.onkey(paddle2.move_up, "w")
#screen.onkey(paddle2.move_down, "s")

while True:
    screen.update()


screen.exitonclick()