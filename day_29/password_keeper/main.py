import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
import json

"""
Schema for the data.json file
{
    "website1": {
        "username1": "password for username1",
        "username2": "password for username2"
    },
    "website2": {
        "username1": "password for username1",
        "username2": "password for username2"
    }
}
"""


def generate_pass():
    small_alpha = 'abcdefghijklmnopqrstuvwxyz'
    cap_alpha = small_alpha.upper()
    nums = '0123456789'
    special_chars = r"!\"#$%&'()*+,-./:;=?@[]^_`{|}\~"
    all_chars = small_alpha + cap_alpha + nums + special_chars
    length = randint(8, 16)
    password = [choice(small_alpha), choice(cap_alpha), choice(nums), choice(special_chars)]
    password += [choice(all_chars) for _ in range(length - 4)]
    # for _ in range(length - 4):
    #     password.append(choice(all_chars))
    shuffle(password)
    password = ''.join(password)
    print(password)
    pass_entry.delete(0, tk.END)  # clear the entry
    pass_entry.insert(tk.END, password)


def add_entries():
    website = website_entry.get().strip().lower()
    username = username_entry.get().strip()
    password = pass_entry.get().strip()

    if website == '' or username == '' or password == '':
        messagebox.showwarning(title='Warning!', message='Oops!!!\nYou are required to fill all the fields.')
        return

    try:
        data[website][username] = password
    except KeyError as exp:
        data[website] = {username: password}

    decision = messagebox.askyesno(title='Save', message='Are you sure?')
    if not decision:
        return
    # if os.path.getsize("passwords.txt") == 0:
    #     with open('passwords.txt', mode='w') as file:
    #         file.write('website,username,password')

    # entry = f'{website} | {username} | {password}\n'
    # print(entry)

    print(data)

    with open('data.json', mode='w') as data_file:
        json.dump(obj=data, fp=data_file, indent=4)
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

    window.clipboard_clear()
    window.clipboard_append(string=password)
    messagebox.showinfo(title='Success', message='Info Added,\nAnd password has been pasted to Clipboard.')


def search_and_show():
    search_site: str = website_entry.get().strip().lower()
    try:
        creds: dict = data[search_site]
    except KeyError:
        messagebox.showwarning(title='Not Found', message='No Credentials exist for ' + search_site)
    else:
        message = ''
        for (email, pswd) in creds.items():
            message += f'Email: {email}\nPassword: {pswd}\n\n'
        messagebox.showinfo(title='Credentials for ' + search_site.title(), message=message)

        # str_var = tk.StringVar()
        # label = tk.Message(window, textvariable=str_var,
        #                    relief=tk.RAISED)
        #
        # # The size of the text determines
        # # the size of the messagebox
        # str_var.set("You can't Change Your Profile Picture ")
        # label.grid()


window = tk.Tk()
window.config(padx=32, pady=40)
window.resizable(width=False, height=False)

try:
    with open('data.json') as file:
        data = json.load(fp=file)
except FileNotFoundError:
    data = {}

lock_img = tk.PhotoImage(file='small_lock.png')
canvas = tk.Canvas(width=400, height=250, highlightthickness=0)
canvas.create_image(200, 125, image=lock_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = tk.Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1, sticky="ew")

search_button = tk.Button(text='Search', command=search_and_show)
search_button.grid(row=1, column=2, sticky='ew')

username_label = tk.Label(text='Email/Username: ')
username_label.grid(row=2, column=0)

username_entry = tk.Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")

pass_label = tk.Label(text='Password:')
pass_label.grid(row=3, column=0)

pass_entry = tk.Entry()
pass_entry.grid(row=3, column=1, columnspan=1, stick='ew')

pass_gen_button = tk.Button(text='Generate', command=generate_pass)
pass_gen_button.grid(row=3, column=2)

add_button = tk.Button(text='Add', command=add_entries)
add_button.grid(row=4, column=1, columnspan=2, stick='ew')

window.mainloop()
