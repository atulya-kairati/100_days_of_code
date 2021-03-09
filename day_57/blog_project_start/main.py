from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    res = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    return res.json()


@app.route('/')
def index_func():
    posts = get_posts()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:_id>')
def show_post_func(_id):
    posts: list = get_posts()
    post = list(filter(lambda x: x['id'] == _id, posts))[0]
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
