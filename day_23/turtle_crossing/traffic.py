from turtle import Turtle
from day_23.turtle_crossing.konstants_utils import *
from random import randint, choice


class Traffic():
    def __init__(self):
        self.cars = []

    def place_cars(self):
        if choice([0,  0, 1]) == 1:
            temp_car = Turtle(shape='square')
            temp_car.color(random_color_hex())
            temp_car.shapesize(stretch_len=2)
            temp_car.up()
            temp_car.goto(240, randint(-180, 180))
            self.cars.append(temp_car)

    def move_traffic(self):
        for i in range(len(self.cars)):
            self.cars[i].bk(10)
            if self.cars[i].xcor() < - 240:
                self.cars[i].ht()
                del self.cars[i]
            if i >= len(self.cars) - 1:
                break
