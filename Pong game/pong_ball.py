from turtle import Turtle
from random import uniform
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_move()
        self.move_speed = 0.05
        
    def set_move(self):
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.setpos(x + self.x_move, y + self.y_move)
    
    def bounce_floor(self):
        self.y_move *= -1
    
    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.99

    def score(self):
        self.home()
        self.bounce_paddle()
        self.move_speed = 0.05