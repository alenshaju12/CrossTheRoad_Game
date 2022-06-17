import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")

screen.tracer(0)
player=Player()
car=Car()
score=Score()

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")

gameison=True
while gameison:
    time.sleep(0.1)
    screen.update()

    car.creat()
    car.move()

    for c in car.allcars:
        if c.distance(player)<20:
            gameison=False
            score.gameover()

    if player.isatfinishline():
        car.level()
        score.level+=1
        score.cl()



screen.exitonclick()