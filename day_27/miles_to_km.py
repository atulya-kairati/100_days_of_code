import tkinter

window = tkinter.Tk()
window.config(padx=16, pady=8)
window.title('Miles to Kilometer')


def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def calculate():
    dist: str = miles.get()
    if not is_float(dist):
        return
    km['text'] = round(eval(f'{dist}*1.609'), ndigits=1)


miles = tkinter.Entry(width=12)
miles.grid(row=0, column=1)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(row=0, column=2)

equals_label = tkinter.Label(text='is equal to')
equals_label.grid(row=1, column=0)

km = tkinter.Label(text='0', width=12, pady=4)
km.grid(row=1, column=1)

km_label = tkinter.Label(text='Km')
km_label.grid(row=1, column=2)

calc_button = tkinter.Button(text='Calculate', command=calculate)
calc_button.grid(row=2, column=1)


window.mainloop()
