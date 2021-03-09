from flask import Flask
from flask import render_template
from flask import request
import requests
from datetime import datetime
from day_60.blog_with_contacts.my_mailer import sendmail

app = Flask(__name__)
year = datetime.now().year


@app.route('/home')
@app.route('/')
def index_page():
    res_json = requests.get(url='https://api.npoint.io/43644ec4f0013682fc0d').json()
    return render_template('index.html', posts=res_json, year=year)


@app.route('/about')
def about_page():
    return render_template('about.html', year=year)


@app.route('/contact')
def contact_page():
    return render_template('contact.html', year=year)


@app.route('/post/<int:_id>')
def post_page(_id):
    res_json = requests.get(url='https://api.npoint.io/43644ec4f0013682fc0d').json()
    post = list(filter(lambda x: x['id'] == _id, res_json))[0]
    return render_template('post.html', year=year, post=post)


@app.route("/msg-sent", methods=['POST'])
def msg_sent_func():
    sendmail(request.form)
    return render_template('msg-sent.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
