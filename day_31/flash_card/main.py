import random
import tkinter as tk
from tkinter import messagebox

import pandas

from day_31.flash_card.constants import *

last_word = None
flag = True


# back_card_kargs = {"fill": "white", "image"}


def refill():
    global words
    if len(words) == 0:
        messagebox.showinfo(title='Hurray!!', message='You learned all the Words, You can play again to revise.')
        words = data.index.to_list()

    with open('word_to_learn.txt', 'w') as file:
        file.write('\n'.join(words))


def show_word():
    print(words)
    refill()
    word = random.choice(words)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word, fill='white')
    canvas.itemconfig(card, image=card_back)
    global flag
    flag = True
    window.after(3000, show_meaning, word)


def show_meaning(word: str):
    global last_word
    last_word = word
    meaning = data[data.index == word].iloc[0]['hindi']
    print(meaning)
    canvas.itemconfig(title_text, text='Hindi', fill='black')
    canvas.itemconfig(word_text, text=meaning, fill='black')
    canvas.itemconfig(card, image=card_front)
    global flag
    flag = False


def tick_func():
    if flag:
        print('Not yet baby')
        return
    words.remove(last_word)

    show_word()


def cross_func():
    if flag:
        print('Not yet baby')
        return
    show_word()


data = pandas.read_csv('smalldata.csv', index_col=1)
print(data.iloc[1]['hindi'])

try:
    with open('word_to_learn.txt') as file:
        words = file.read().split('\n')
        if words[0] == '':
            words.remove('')
except FileNotFoundError as exp:
    words = data.index.to_list()

print(len(words))

window = tk.Tk()
window.config(padx=56, pady=40, bg=GREEN)

card_front = tk.PhotoImage(file='card_front.png')
card_back = tk.PhotoImage(file='card_back.png')
cross_img = tk.PhotoImage(file='smallcross.png')
tick_img = tk.PhotoImage(file='smalltick.png')

canvas = tk.Canvas(height=280, width=520, highlightthickness=0, bg=GREEN)
card = canvas.create_image(275, 140, image=card_back)
title_text = canvas.create_text(265, 50, text='title', font=TITLE_FONT, fill='white')
word_text = canvas.create_text(255, 150, text='Word', font=WORD_FONT, fill='white')
canvas.grid(row=0, column=0, columnspan=2)

cross_button = tk.Button(image=cross_img, highlightthickness=0, bg=GREEN, command=cross_func)
cross_button.grid(row=1, column=0)

tick_button = tk.Button(image=tick_img, highlightthickness=0, bg=GREEN, command=tick_func)
tick_button.grid(row=1, column=1)

show_word()

window.mainloop()
