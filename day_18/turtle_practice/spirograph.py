import turtle as tr
from random import randint

s = tr.getscreen()
t = tr.Turtle()
s.colormode(255)
tr.bgcolor('black')
t.speed('fastest')
t.pensize(1)


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )


def spirograph(size, no_of_circles=20):
    for _ in range(no_of_circles):
        t.color(random_color())
        t.circle(size)
        t.rt(360 / no_of_circles)


spirograph(100, 100)

tr.mainloop()
