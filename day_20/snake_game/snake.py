from turtle import Turtle

STEP = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake(20)
        self.head = self.body[0]

    def create_snake(self, initial_len):
        for i in range(initial_len):
            block = Turtle(shape='square')
            block.up()
            print(block.heading())
            # block.speed('fastest')
            block.color('white')
            block.goto(-20 * i, 0)
            self.body.append(block)

    def get_big(self):
        self.body.append(self.body[-1].clone())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())
        self.head.fd(STEP)

    def up(self):
        if self.head.heading() in (90, 270):
            return
        print('UP')
        self.head.setheading(90)

    def down(self):
        if self.head.heading() in (90, 270):
            return
        print('DOWN')
        self.head.setheading(270)

    def right(self):
        if self.head.heading() in (0, 180):
            return
        print('RIGht')
        self.head.setheading(0)

    def left(self):
        if self.head.heading() in (0, 180):
            return
        print('LEFT')
        self.head.setheading(180)