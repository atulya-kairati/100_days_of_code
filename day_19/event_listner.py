from turtle import Turtle, Screen

t = Turtle()
s = Screen()
# t.speed('fastest')


def move_forward():
    t.fd(10)


def move_backward():
    t.bk(10)


def turn_rightward():
    t.rt(5)


def turn_leftward():
    t.lt(5)


def clear():
    t.home()
    t.clear()


s.listen()
s.onkey(key='w', fun=move_forward)
s.onkey(key='s', fun=move_backward)
s.onkey(key='a', fun=turn_leftward)
s.onkey(key='d', fun=turn_rightward)
s.onkey(key='c', fun=clear)


s.exitonclick()
