from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.bounce_y()
    scoreboard.update_scoreboard()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = 0.04

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed = 0.04

screen.exitonclick()
