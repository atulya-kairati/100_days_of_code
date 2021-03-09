import turtle as tr
from random import randint


def polygon(side, sidenum):
    s = tr.getscreen()
    t = tr.Turtle()
    s.colormode(255)
    t.color(
        randint(0, 256),
        randint(0, 256),
        randint(0, 256),
    )
    angle = 360 / sidenum
    for _ in range(sidenum):
        t.fd(side)
        t.rt(angle)


for i in range(4, 20):
    polygon(100, i)

tr.mainloop()
