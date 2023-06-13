from turtle import Screen
from time import sleep
from pong_player import Player
from pong_ball import Ball
from pong_score import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0)
left_player = Player((-350, 0))
right_player = Player((350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(right_player.up, "Up")
screen.onkey(right_player.down, "Down")
screen.onkey(left_player.up, "w")
screen.onkey(left_player.down, "s")
while score.not_game_over():
    screen.update()
    sleep(ball.move_speed)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_floor()
    
    if (ball.distance(right_player) < 50 and ball.xcor() > 320) or (ball.distance(left_player) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.score()
        score.new_score("L")

    if ball.xcor() < -380:
        ball.score()
        score.new_score("R")

score.game_over()

screen.exitonclick()