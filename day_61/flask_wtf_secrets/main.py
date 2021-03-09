from flask import (
    Flask,
    render_template
)
from flask_bootstrap import Bootstrap
from day_61.flask_wtf_secrets.my_form import MyLoginForm

app = Flask(__name__)
app.secret_key = 'yoyo'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', "GET"])
def login():
    mail = 'atulya54321@gmail.com'
    pswd = 'laudalasun'
    login_form = MyLoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == mail and login_form.pswd.data == pswd:
            return render_template('success.html')
        return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
