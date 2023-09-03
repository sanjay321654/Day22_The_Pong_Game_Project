from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=20, stretch_len=20)
        self.color("white")
        self.setheading(45)
        self.goto(position)
