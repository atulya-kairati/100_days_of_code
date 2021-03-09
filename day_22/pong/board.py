from turtle import Turtle
from day_22.pong.konstants import *


class Board(Turtle):

    def __init__(self, coord: tuple, len_factor=6):
        super().__init__(shape='square')
        self.color('white')
        self.up()
        self.goto(coord)
        self.setheading(90)
        self.len_factor = len_factor
        self.shapesize(stretch_len=len_factor)
        self.lives = 3

    def auto_step(self):
        if self.ycor() < -SCREEN_HEIGHT//2 + (TURTLE_EDGE_LEN * self.len_factor)//2:
            self.setheading(90)
        elif self.ycor() > SCREEN_HEIGHT//2 - (TURTLE_EDGE_LEN * self.len_factor)//2:
            self.setheading(270)

        self.fd(20)

    def manual_up(self):
        if self.ycor() > SCREEN_HEIGHT // 2 - (TURTLE_EDGE_LEN * self.len_factor)//2:
            return
        self.fd(20)

    def manual_down(self):
        if self.ycor() < -SCREEN_HEIGHT // 2 + (TURTLE_EDGE_LEN * self.len_factor)//2:
            return
        self.bk(20)


