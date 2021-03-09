import tkinter as tk
import requests
import html
from tkinter import messagebox

# nsew = north south east west
current_quiz_no = 0
score = 0
TRIVIA_API = 'https://opentdb.com/api.php?amount=10&type=boolean'
quiz = []


def get_bool(bool_str: str):
    return bool_str.lower() == 'true'


def increment_score():
    global score
    score += 1
    score_label['text'] = f'Score: {score}'


def get_quiz():
    print('getting quiz...')
    response = requests.get(url=TRIVIA_API)
    response.raise_for_status()
    questions = response.json()['results']
    return [{"question": html.unescape(ques["question"]), "answer": get_bool(ques['correct_answer'])} for ques in questions]


def show_ques():
    window.config(bg=default_color_bg)
    global current_quiz_no
    if current_quiz_no >= len(quiz):
        choice = messagebox.askyesno(message=f'You Scored {score} out of {len(quiz)}\nDo you want to play again?')
        if choice:
            start_quiz()
        else:
            window.destroy()
        return
    ques = quiz[current_quiz_no]['question']
    ans = quiz[current_quiz_no]['answer']
    canvas.itemconfig(ques_text, text=ques)
    current_quiz_no += 1


def wrong_pressed():
    if not quiz[current_quiz_no - 1]['answer']:
        increment_score()
        window.config(bg='green')
    else:
        window.config(bg='red')
    window.after(ms=100, func=show_ques)


def right_pressed():
    if quiz[current_quiz_no - 1]['answer']:
        increment_score()
        window.config(bg='green')
    else:
        window.config(bg='red')
    window.after(ms=100, func=show_ques)


def start_quiz():
    global current_quiz_no, score, quiz
    score_label['text'] = 'Score: 0'
    current_quiz_no = score = 0
    quiz = get_quiz()
    show_ques()


window = tk.Tk()
default_color_bg = window['bg']
window.config(padx=32, pady=24)

score_label = tk.Label(text='Score: 0', anchor='w')
score_label.grid(row=0, column=0, stick='w')

canvas = tk.Canvas(width=320, height=240, bg='white')
ques_text = canvas.create_text(160, 120, width=280, text='Loading....')
canvas.grid(row=1, column=0, columnspan=2, pady=16)

wrong_button = tk.Button(text='✘', font=('Ariel', 40, 'bold'), bg='red', command=wrong_pressed)
wrong_button.grid(row=2, column=0, stick='news', padx=8)

right_button = tk.Button(text='✔', font=('Ariel', 40, 'bold'), bg='green', command=right_pressed)
right_button.grid(row=2, column=1, stick='news', padx=8)

start_quiz()

window.mainloop()
