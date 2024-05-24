from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()
ball = Ball((0, 0))
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# ***Detect collision with wall***
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# ***Detect collision with paddle***
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()




screen.exitonclick()