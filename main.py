from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
bg_pic = "pong.gif"
screen.bgpic(bg_pic)
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-383, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score = ScoreBoard()
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect the collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()

    # Detect the collision with the right paddle.
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.x_bounce()

    # Detect the collision with the left paddle.
    if ball.distance(l_paddle) <= 50 and ball.xcor() - 320:
        ball.x_bounce()

    # Detect right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.l_point()

    # Detect left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_ball_position()
        score.r_point()

screen.exitonclick()
