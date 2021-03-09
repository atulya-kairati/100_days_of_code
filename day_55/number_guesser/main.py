from flask import Flask
from random import randint

app = Flask(__name__)
g_num = 0


@app.route('/')
def home():
    global g_num
    g_num = randint(0, 9)
    return '' \
           '<img height=240 src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
           '<p>Go to <a href="http://localhost:5000/8">http://localhost:5000/8</a> to guess 8.</p>'


@app.route('/<int:num>')
def guess(num):
    if num > g_num:
        msg = 'You guessed too high.'
        img_link = 'https://i.redd.it/nm4bb2yw9c941.jpg'
    elif num < g_num:
        msg = 'You guessed too low.'
        img_link = 'https://i.redd.it/n0h6ijzuxtu21.jpg'
    else:
        msg = 'You guessed right.'
        img_link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRz0Rc1T4n8Aw9AYbNpf8Q8lt1po6FIKjxeg&usqp=CAU'

    return f'<h1>{msg}</h1>' \
           f'<img height=240 src="{img_link}"></br>' \
           f'<a href="http://localhost:5000/">Play Again</a>'


if __name__ == '__main__':
    app.run(debug=True)
