from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle miss and ball hits the wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # detect left paddle miss and ball hits the wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()