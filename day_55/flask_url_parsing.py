from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "HOHOHO"


# url parsing
@app.route('/name/<name>')
def my_route(name):
    return name


@app.route('/<int:num>')
def print_num(num):
    return f'number is {num}'


@app.route('/name/<name>/<int:num>')
def complex_route(name, num):
    return f'{name}\'s number is {num}'


@app.route('/path/<path:path>')
def get_path(path):
    return path


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
