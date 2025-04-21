from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # controls the animation (turn off the
# animation) of pong going from the middle to the location.
# Now we have to manually update
# the screen and refresh it every single time.


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# top_paddle = Paddle((100,100))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # ball.speed("fastest")
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()