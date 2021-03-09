from turtle import Turtle, Screen
from random import randint

s = Screen()
s.bgcolor('black')
s.setup(width=620, height=620)
t = Turtle(shape='turtle')
t.width(8)
t.speed('fastest')


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )


def random_color_hex():
    return f'#{hex(randint(16, 255))[2:]}{hex(randint(16, 255))[2:]}{hex(randint(16, 255))[2:]}'


def random_step(turt, length):
    turt.color(random_color_hex())
    r = randint(-1, 1)
    turt.rt(120 * r)
    turt.fd(length)
    if turt.xcor() > 300 or turt.xcor() < -300 or turt.ycor() > 300 or turt.ycor() < -300:
        turt.rt(180)
        turt.home()
        turt.clear()
        print('shit')


while True:
    random_step(t, 20)
