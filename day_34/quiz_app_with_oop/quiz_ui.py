import tkinter as tk
from tkinter import messagebox

from day_34.quiz_app_with_oop.quiz_brain import QuizBrain


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.default_color_bg = self.window['bg']
        self.window.config(padx=32, pady=24)
        self.score_label = tk.Label(text='Score: 0', anchor='w')
        self.score_label.grid(row=0, column=0, stick='w')

        self.canvas = tk.Canvas(width=320, height=240, bg='white')
        self.ques_text = self.canvas.create_text(160, 120, width=280, text='Loading....')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=16)

        self.wrong_button = tk.Button(text='✘', font=('Ariel', 40, 'bold'), bg='red', command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=0, stick='news', padx=8)

        self.right_button = tk.Button(text='✔', font=('Ariel', 40, 'bold'), bg='green', command=self.right_pressed)
        self.right_button.grid(row=2, column=1, stick='news', padx=8)

        self.start_quiz()

        self.window.mainloop()

    def start_quiz(self):
        self.score_label['text'] = 'Score: 0'
        self.quiz_brain.reset()
        self.quiz_brain.get_quiz()
        print(self.quiz_brain.quiz)
        self.show_ques()

    def wrong_pressed(self):
        if self.quiz_brain.check_current_answer(answer=False):
            self.quiz_brain.increment_score()
            self.window.config(bg='green')
        else:
            self.window.config(bg='red')
        self.window.after(ms=100, func=self.show_ques)

    def right_pressed(self):
        if self.quiz_brain.check_current_answer(answer=True):
            self.quiz_brain.increment_score()
            self.window.config(bg='green')
        else:
            self.window.config(bg='red')
        self.window.after(ms=100, func=self.show_ques)

    def show_ques(self):
        self.window.config(bg=self.default_color_bg)
        self.score_label['text'] = f'Score: {self.quiz_brain.score}'
        try:
            question = self.quiz_brain.get_current_question()
        except ValueError as exp:
            choice = messagebox.askyesno(
                message=f'You Scored {self.quiz_brain.score} out'
                        f' of {len(self.quiz_brain.quiz)}\nDo you want to play again?'
            )
            if choice:
                self.start_quiz()
            else:
                self.window.destroy()

            return
        ques = question['question']
        ans = question['answer']
        self.canvas.itemconfig(self.ques_text, text=ques)