from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditor, CKEditorField
import requests
from datetime import datetime
from day_60.blog_with_contacts.my_mailer import sendmail

app = Flask(__name__)
db = SQLAlchemy(app)
Bootstrap(app)
ckeditor = CKEditor(app)

app.config['SECRET_KEY'] = '32432f3w4r3453r34535'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

year = datetime.now().year


def get_formatted_date():
    today = datetime.today()
    date = today.strftime('%B %d, %Y')
    return date


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            title=data.get('title'),
            subtitle=data.get('subtitle'),
            date=data.get('date'),
            author=data.get('author'),
            body=data.get('body'),
            img_url=data.get('img_url')
        )

    def get_dict(self):
        # cafe_dict = self.__dict__
        # # print(cafe_dict)
        # del cafe_dict['_sa_instance_state']
        # return cafe_dict
        # above commented method works but its very buggy

        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'date': self.date,
            'author': self.author,
            'body': self.body,
            'img_url': self.img_url,
        }


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    ph_num = StringField(label='Phone Number', validators=[DataRequired(), Length(min=10)])
    msg = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')


class PostEditorForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author Name', validators=[DataRequired()])
    img_url = StringField(label='Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField(label='Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='Post')

    def get_from_data(self):
        return {
            'title': self.title.data,
            'subtitle': self.subtitle.data,
            'author': self.author.data,
            'img_url': self.img_url.data,
            'body': self.body.data,
        }


db.create_all()


@app.route('/home')
@app.route('/')
def index_page():
    # res_json = requests.get(url='https://api.npoint.io/43644ec4f0013682fc0d').json()
    blog_objs = BlogPost.query.all()
    blog_posts = [blog_obj.get_dict() for blog_obj in blog_objs]
    print(blog_posts)
    return render_template('index.html', posts=blog_posts, year=year)


@app.route('/about')
def about_page():
    return render_template('about.html', year=year)


@app.route('/contact', methods=['GET', 'POSt'])
def contact_page():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        # TODO: Send Mail
        return redirect(url_for('msg_sent_func'))
    return render_template('contact.html', year=year, form=contact_form)


@app.route('/post/<int:_id>')
def post_page(_id):
    # res_json = requests.get(url='https://api.npoint.io/43644ec4f0013682fc0d').json()
    # post = list(filter(lambda x: x['id'] == _id, res_json))[0]
    post = BlogPost.query.get(_id)
    # print(post.get_dict())
    return render_template('post.html', year=year, post=post)


@app.route("/msg-sent", methods=['GET'])
def msg_sent_func():
    return render_template('msg-sent.html', year=year)


@app.route("/add", methods=['GET', 'POST'])
def add_func():
    editor_form = PostEditorForm()
    if editor_form.validate_on_submit():
        post_data = editor_form.get_from_data()
        date = get_formatted_date()
        post_data['date'] = date
        # print(post_data)
        new_post = BlogPost.create_from_dict(data=post_data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index_page'))
    return render_template('make-post.html', year=year, form=editor_form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = BlogPost.query.get(id)
    # print(f'>>> {post.title}')
    editor_form = PostEditorForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body,
    )
    if editor_form.validate_on_submit():
        edited_post_data = editor_form.get_from_data()
        post.title = edited_post_data.get('title')
        post.subtitle = edited_post_data.get('subtitle')
        post.author = edited_post_data.get('author')
        post.img_url = edited_post_data.get('img_url')
        post.body = edited_post_data.get('body')
        db.session.commit()
        return redirect(url_for('post_page', _id=id))
    return render_template('make-post.html', year=year, form=editor_form)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_func(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index_page'))


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
