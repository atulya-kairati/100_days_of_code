from turtle import Turtle, Screen
from random import randint, shuffle

t = Turtle(visible=False)
w_height = 480
w_width = 640
gap = 50
t.up()
t.goto(300, -240)
t.down()
t.goto(300, 240)
s = Screen()

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
shuffle(colors)


def ready_turtles(num: int):
    turtles = []
    for i in range(num):
        temp = Turtle(shape='turtle')
        temp.color(colors[i])
        temp.up()
        temp.goto(-(w_width//2 - 20), (gap * ((num - 1) / 2 - i)))
        turtles.append(temp)
    return turtles


def turtles_go(turtles: list):
    flag = False
    winner = 0
    while True:
        for i in range(len(turtles)):
            turtles[i].fd(randint(1, 10))
            if turtles[i].xcor() >= w_width//2 - 35:
                flag = True
                winner = i
                break
        if flag:
            break
    return winner


s.setup(width=w_width, height=w_height)
s.title('Turtle Racer')
user_bet = s.textinput(title='Make Your Bet', prompt='Which color turtle will win the race?')
print(user_bet)

racers = ready_turtles(6)
uber_turtle = turtles_go(racers)
print(f'Winner is {colors[uber_turtle]} turtle')
print(f'You {"Win" if colors[uber_turtle] == user_bet else "Lose"}')

s.exitonclick()
