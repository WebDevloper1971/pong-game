from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time

paddle_left = (-350, 0)
paddle_right = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

player_1 = Paddle(paddle_left)
player_2 = Paddle(paddle_right)

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()

screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")

screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_1_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player_2_point()
screen.exitonclick()
