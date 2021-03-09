# USING place Layout Managers

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
# window.minsize(width=240, height=320)
# window.maxsize(width=240, height=320)

# label with place
my_label = tkinter.Label(text='MY LABEL')
my_label.place(x=0, y=100)

# button
my_button = tkinter.Button(text='Click Me!!', command=button_func)
my_button.place(x=300, y=400)

# entry
input_field = tkinter.Entry(width=10)
input_field.insert(tkinter.END, 'This is an entry.')
input_field.place(x=20, y=200)

window.mainloop()