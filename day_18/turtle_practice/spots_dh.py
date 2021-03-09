import turtle as tr
from random import choice
import colorgram

pallete = colorgram.extract('dh_mkc.jpg', 30)

pallete = pallete[4: -1]

print(tuple(pallete[0].rgb))

s = tr.getscreen()
t = tr.Turtle()
t.hideturtle()
s.colormode(255)
# tr.bgcolor('black')
t.speed('fastest')
t.pensize(1)

for i in range(-200, 200, 40):
    for j in range(-200, 200, 40):
        t.up()
        t.setpos(i, j)
        t.down()
        t.dot(16, tuple(choice(pallete).rgb))

tr.mainloop()
