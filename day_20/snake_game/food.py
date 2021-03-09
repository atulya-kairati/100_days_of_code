from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('green')
        self.speed('fastest')
        self.goto(x=randint(-300, 300), y=randint(-300, 300))

    def eaten(self):
        self.goto(x=randint(-300, 300), y=randint(-300, 300))
