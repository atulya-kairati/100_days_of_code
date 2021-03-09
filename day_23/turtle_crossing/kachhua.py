from turtle import Turtle


class Kachhua(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.up()
        self.color('blue')
        self.setheading(90)
        self.goto(0, -210)

    def move(self):
        self.fd(10)

    def check_car_collision(self, traffic):
        for car in traffic:
            if abs(self.ycor() - car.ycor()) < 20 and \
                    abs(self.xcor() - car.xcor()) < 30:
                return True
        return False

    def reset(self):
        self.goto(0, -210)