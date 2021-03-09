from turtle import Turtle
FONT = ('Arial', 12, 'normal')
FONT2 = ('Arial', 24, 'bold')
ALIGNMENT = 'left'
ALIGNMENT2 = 'center'


class Banner(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.level = 1
        self.pencolor('black')
        self.up()
        self.goto(-220, 220)
        self.write(f'Level: {self.level}', font=FONT, align=ALIGNMENT)

    def up_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(f'GAME OVER', font=FONT2, align=ALIGNMENT2)
