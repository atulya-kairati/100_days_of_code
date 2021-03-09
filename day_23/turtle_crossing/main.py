from time import sleep
from turtle import Screen

from day_23.turtle_crossing.banner import Banner
from day_23.turtle_crossing.kachhua import Kachhua
from day_23.turtle_crossing.konstants_utils import *
from day_23.turtle_crossing.traffic import Traffic

screen = Screen()
screen.tracer(False)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

traffic = Traffic()
you = Kachhua()
frame_gap = 0.2

banner = Banner()

screen.listen()
screen.onkey(you.move, 'Up')


while True:
    flag = False
    traffic.place_cars()
    traffic.move_traffic()
    screen.update()

    if you.check_car_collision(traffic.cars):
        print(you.ycor())
        screen.update()
        break

    if you.ycor() > 240:
        you.reset()
        banner.up_level()
        frame_gap -= frame_gap*0.1
    sleep(frame_gap)

banner.game_over()
screen.exitonclick()
