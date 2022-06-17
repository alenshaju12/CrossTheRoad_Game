from  turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.level=1
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-280,260)
        self.cl()

    def cl(self):
        self.clear()
        self.write(f"Level = {self.level}",align="left", font=("arial",20, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("arial", 20, "normal"))