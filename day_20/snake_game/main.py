from turtle import Screen
from time import sleep

from day_20.snake_game.food import Food
from day_20.snake_game.score import ScoreBoard
from day_20.snake_game.snake import Snake

w_width = w_height = 640
screen = Screen()
screen.tracer(0)
screen.title('Snake Game')
screen.bgcolor('black')
screen.setup(width=w_width, height=w_height)

noodle = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(noodle.up, 'Up')
screen.onkey(noodle.down, 'Down')
screen.onkey(noodle.right, 'Right')
screen.onkey(noodle.left, 'Left')

while True:
    screen.update()
    noodle.move()
    sleep(0.1)

    # Detect Collision with food
    if noodle.head.distance(food) < 15:
        print('nom nom')
        food.eaten()
        noodle.get_big()
        score_board.increase_score()

    # Detect Collision with wall
    if 310 < noodle.head.xcor() or noodle.head.xcor() < -310 \
            or noodle.head.ycor() < -310 or noodle.head.ycor() > 320:
        break

    # Detect Collision with own body
    flag = False
    for block in noodle.body[1:]:
        if noodle.head.distance(block) < 10:
            flag = True
            break
    if flag:
        break
score_board.game_over()
screen.exitonclick()
