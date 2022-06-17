from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.gotostart()
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def gotostart(self):
        self.goto(0, -280)

    def isatfinishline(self):
        if self.ycor()>280:
            self.gotostart()
            return True
        else:
            return False