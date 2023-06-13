from turtle import Turtle
class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(position)
    
    def up(self):
        y = self.ycor()
        x = self.xcor()
        self.setpos(x, y + 20)
    
    def down(self):
        y = self.ycor()
        x = self.xcor()
        self.setpos(x, y - 20)

