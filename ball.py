from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.x_move = 8
        self.y_move = 8
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_bounce()
