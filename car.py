from turtle import Turtle
import random

COLORS=["red","green","blue","yellow","purple"]

class Car():

    def __init__(self):
        self.allcars=[]
        self.carspeed=5

    def creat(self):
        if 1==(random.randint(0,6)):
            car=Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            y=random.randint(-240,240)
            car.goto(300,y)
            self.allcars.append(car)

    def move(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def level(self):
        self.carspeed += 5