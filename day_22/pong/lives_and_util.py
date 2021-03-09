from turtle import Turtle
from day_22.pong.konstants import *

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
FONT2 = ('Arial', 24, 'bold')


class LifeAndUtils(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.pencolor('white')
        self.up()
        self.goto(0, SCREEN_HEIGHT//2 - 40)
        self.write('3    3', font=FONT, align=ALIGNMENT)

    def set_life_banner(self, banner: str):
        self.clear()
        self.goto(0, SCREEN_HEIGHT//2 - 40)
        self.score += 1
        self.write(banner, font=FONT, align=ALIGNMENT)

    def game_over(self, status: str):
        self.goto(0, 0)
        self.pencolor('red')
        self.write(status, font=FONT2, align=ALIGNMENT)