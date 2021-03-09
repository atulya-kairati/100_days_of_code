from turtle import Screen, Turtle
from time import sleep
from day_22.pong.lives_and_util import LifeAndUtils
from day_22.pong.ball import Ball
from day_22.pong.board import Board
from day_22.pong.konstants import *


screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor('black')
screen.tracer(False)

divider = Turtle(shape='square')
divider.color('white')
divider.shapesize(stretch_len=0.1, stretch_wid=40)

# make_board
auto_board = Board((-SCREEN_WIDTH//2 + 10, 0), len_factor=2)
user_board = Board((SCREEN_WIDTH//2 - 15, 0), len_factor=5)

# make ball
ball = Ball()

screen.listen()
screen.onkey(fun=user_board.manual_up, key='Up')
screen.onkey(fun=user_board.manual_down, key='Down')
life_utils = LifeAndUtils()

while True:
    auto_board.auto_step()
    screen.update()
    ball.move()
    ball.check_board_bounce(board=auto_board)
    ball.check_board_bounce(board=user_board)
    ball.check_wall_bounce()
    sleep(ball.frame_time_gap)

    if ball.xcor() < -SCREEN_WIDTH//2:
        auto_board.lives -= 1
        user_board.lives += 1
        del ball
        ball = Ball()
    elif ball.xcor() > SCREEN_WIDTH//2:
        user_board.lives -= 1
        auto_board.lives += 1
        del ball
        ball = Ball()

    life_utils.set_life_banner(banner=f'{auto_board.lives}    {user_board.lives}')

    if auto_board.lives < 1:
        life_utils.game_over(status='YOU WIN')
        break
    elif user_board.lives < 1:
        life_utils.game_over(status='YOU LOSE')
        break
screen.exitonclick()
