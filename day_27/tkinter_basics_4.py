# USING grid Layout Manager

import tkinter

click_counter = 0


def button_func():
    print('button clicked')
    global click_counter
    click_counter += 1
    my_button['text'] = f'I was clicked {click_counter} times'
    my_label['text'] = input_field.get()


window = tkinter.Tk()
window.title('Sample Window')
window.config(padx=16, pady=8)
# window.minsize(width=240, height=320)
# window.maxsize(width=240, height=320)

# label with place
my_label = tkinter.Label(text='MY LABEL')
my_label.grid(row=0, column=0)

# button
my_button = tkinter.Button(text='Click Me!!', command=button_func)
my_button.grid(row=1, column=1)

# entry
input_field = tkinter.Entry(width=10)
input_field.insert(tkinter.END, 'This is an entry.')
input_field.grid(row=2, column=3)

new_button = tkinter.Button(text='NEW BUTTON')
new_button.grid(row=0, column=2)

window.mainloop()