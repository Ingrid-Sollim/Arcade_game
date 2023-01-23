from turtle import Turtle
#Start Position
X0 = 375
Y0 = 0
class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()
        self.goto(X0, Y0)

    def move_up(self):
        ny = self.ycor() + 20
        self.goto(X0, ny)
#        self.speed("fast")

    def move_down(self):
        ny = self.ycor() - 20
        self.goto(X0, ny)

