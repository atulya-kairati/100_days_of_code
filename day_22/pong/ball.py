from turtle import Turtle
from day_22.pong.konstants import *
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('yellow')
        self.setheading(randint(-60, 60))
        self.up()
        self.frame_time_gap = 0.1

    def check_board_bounce(self, board):
        if abs(board.xcor() - self.xcor()) < 20 and \
                abs(board.ycor() - self.ycor()) < (TURTLE_EDGE_LEN * board.len_factor)//2:
            heading = self.heading()
            self.frame_time_gap = self.frame_time_gap - self.frame_time_gap*0.1
            if 90 < heading < 270:
                self.setheading(180 - heading)
            elif 0 <= heading < 90:
                self.setheading((90 - heading)*2 + heading)
            elif 270 < heading < 360:
                self.setheading(360 - heading + 180)

    def check_wall_bounce(self):
        heading = self.heading()
        if self.ycor() > SCREEN_HEIGHT//2 - 10 or self.ycor() < -(SCREEN_HEIGHT//2 - 10):
            self.setheading(360 - heading)

    def move(self):
        self.fd(20)
