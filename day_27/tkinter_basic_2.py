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
window.minsize(width=240, height=320)
window.maxsize(width=240, height=320)

# label
my_label = tkinter.Label(text='MY LABEL')
my_label.pack()

# button
my_button = tkinter.Button(text='Click Me!!', command=button_func)
my_button.pack()

# entry
input_field = tkinter.Entry(width=10)
input_field.pack()
input_field.insert(tkinter.END, 'This is an entry.')

# text
text_field = tkinter.Text(width=10, height=5)
text_field.insert(tkinter.END, 'Multi\nline\ntext')
text_field.pack()
print(text_field.get('1.0', tkinter.END))


# spinbox
def spinbox_func():
    print(spinbox.get())


spinbox = tkinter.Spinbox(width=5, from_=0, to=100)
spinbox.config(command=spinbox_func)
spinbox.pack()


# scale
def scale_func(val):
    print(val)


scale = tkinter.Scale(from_=0, to=100, command=scale_func)
scale.pack()

window.mainloop()
