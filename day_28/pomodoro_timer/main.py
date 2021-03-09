import tkinter
from day_28.pomodoro_timer.constants import *

reps = 0
timer = None
is_running = False


def countdown(count):
    global timer
    if count < 0:
        start()
        return
    mins, secs = divmod(count, 60)
    canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(mins, secs))
    timer = window.after(1000, countdown, count - 1)


def start():
    global reps, is_running
    if is_running:
        return

    reps += 1
    is_running = True

    if reps % 8 == 0:
        increase_ticks()
        time = LONG_BREAK_MIN * 60
        timer_label.config(fg=RED, text='Break')
    elif reps % 2 == 0:
        increase_ticks()
        time = SHORT_BREAK_MIN * 60
        timer_label['text'] = 'Break'
        timer_label.config(fg=PINK, text='Break')
    else:
        time = WORK_MIN * 60
        timer_label['text'] = 'Work'
        timer_label.config(fg=GREEN, text='Work')
    countdown(time)


def increase_ticks():
    ticks['text'] = ticks['text'] + '✔'


def reset():
    global reps, is_running
    reps = 0
    is_running = False

    if not timer:
        return
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    ticks['text'] = ''


window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=80, pady=40, bg=YELLOW)
# window.minsize(width=400, height=400)

timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, '40', 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='small_tomato.png')
canvas.create_image(125, 125, image=tomato_img)
timer_text = canvas.create_text(125, 150, text='00:00', fill='white', font=(FONT_NAME, '40', 'bold'))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text='START', bg=YELLOW, highlightbackground=YELLOW, fg=RED,
                              font=(FONT_NAME, '12', 'bold'), command=start)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text='RESET', bg=YELLOW, highlightbackground=YELLOW, fg=RED,
                              font=(FONT_NAME, '12', 'bold'), command=reset)
reset_button.grid(row=2, column=2)

ticks = tkinter.Label(text='', font=(FONT_NAME, '20', 'bold'), bg=YELLOW, fg=GREEN)
ticks.grid(row=3, column=1)

# countdown(5)

window.mainloop()
