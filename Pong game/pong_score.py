from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.right_player = 0
        self.left_player = 0
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(0, 240)
        self.write("0 X 0", False, "center", ("Arial", 30, "normal"))
    
    def new_score(self, player):
        self.clear()
        if player == "R":
            self.right_player += 1
        else:
            self.left_player += 1
        self.write(f"{self.left_player} X {self.right_player}", False, "center", ("Arial", 30, "normal"))

    def not_game_over(self):
        if self.right_player > 10 or self.left_player > 10:
            return False
        else:
            return True
    
    def game_over(self):
        self.setpos(0, 170)
        self.color("red")
        self.write("Game Over", False, "center", ("Arial", 40, "normal"))
        self.home()
        self.color("orange")
        if self.right_player > self.left_player:
            self.write("Right player wins!", False, "center", ("Arial", 50, "normal"))
        else:
            self.write("Left player wins!", False, "center", ("Arial", 50, "normal"))