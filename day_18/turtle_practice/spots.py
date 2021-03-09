import turtle as tr
from random import randint

s = tr.getscreen()
t = tr.Turtle()
s.colormode(255)
# tr.bgcolor('black')
t.speed('fastest')
t.pensize(1)


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )


for i in range(-100, 100, 10):
    for j in range(-100, 100, 10):
        t.up()
        t.setpos(i, j)
        t.down()
        t.dot(5, random_color())

tr.mainloop()
