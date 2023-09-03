from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)

screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("green")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
