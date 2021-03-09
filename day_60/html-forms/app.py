from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_func():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_func():
    if request.method == 'POST':
        usrname = request.form.get('name')
        pswd = request.form.get('pswd')
        return f"Your name is: {usrname}\nYour Password is: {pswd}" 
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
