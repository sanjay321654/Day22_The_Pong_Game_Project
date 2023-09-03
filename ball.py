from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")

    def move(self):
        if self.xcor() < 350 and self.ycor() < 280:

            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)