from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')
FONT2 = ('Arial', 24, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        with open('highscore.txt', mode='r') as file:
            data = file.read()
            self.highscore = int(data) if data != '' else 0
        self.pencolor('white')
        self.up()
        self.goto(0, 300)
        self.write(f'Score: {self.score} | High Score: {self.highscore}', font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.goto(0, 300)
        self.score += 1
        self.write(f'Score: {self.score} | High Score: {self.highscore}', font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.highscore:
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.score))
        self.pencolor('red')
        self.write(f'GAME OVER', font=FONT2, align=ALIGNMENT)
