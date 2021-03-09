import tkinter
from time import sleep

window = tkinter.Tk()
window.title('Tkinter Window')
window.minsize(width=480, height=640)
window.config(padx=24, pady=24)

# label
my_label = tkinter.Label(text='I am a Label', font=('Arial', 32, 'italic'))
my_label.pack(side='bottom')
my_label.config(padx=24, pady=24)

# changing attributes of a tkinter component
my_label.config(text='Label Changed')
my_label['text'] = 'Label Changed Again'

window.mainloop()
