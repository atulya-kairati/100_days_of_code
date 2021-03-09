from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditor, CKEditorField
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from day_60.blog_with_contacts.my_mailer import sendmail
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import sqlalchemy
# from sqlalchemy.orm import relationship
from functools import wraps

app = Flask(__name__)
db = SQLAlchemy(app)
Bootstrap(app)
ckeditor = CKEditor(app)

app.config['SECRET_KEY'] = '32432f3w4r3453r34535'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

year = datetime.now().year

login_manager = LoginManager()
login_manager.init_app(app)

def get_formatted_date():
    today = datetime.today()
    date = today.strftime('%B %d, %Y')
    return date


# user loader for FLask Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(160))
    name = db.Column(db.String(1000))
    post = db.relationship('BlogPost', backref="author")
    comments = db.relationship('Comment', backref="author")

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref="parent_post")


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


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))

class RegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Send')

    def get_form_data(self):
        return {
            'name': self.name.data,
            'email': self.email.data,
            'password': self.password.data
        }


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Send')

    def get_form_data(self):
        return {
            'email': self.email.data,
            'password': self.password.data
        }


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    ph_num = StringField(label='Phone Number', validators=[DataRequired(), Length(min=10)])
    msg = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')


class CommentForm(FlaskForm):
    comment = CKEditorField(label='Comment', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class PostEditorForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    # author = StringField(label='Author Name', validators=[DataRequired()])
    img_url = StringField(label='Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField(label='Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='Post')

    def get_from_data(self):
        return {
            'title': self.title.data,
            'subtitle': self.subtitle.data,
            # 'author': self.author.data,
            'img_url': self.img_url.data,
            'body': self.body.data,
        }


db.create_all()


def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        if current_user.get_id() != "1":
            return abort(status=403)
        return function(*args, **kwargs)
    return wrapper


@app.route('/home')
@app.route('/')
def index_page():
    # res_json = requests.get(url='https://api.npoint.io/43644ec4f0013682fc0d').json()
    blog_objs = BlogPost.query.all()
    blog_posts = [blog_obj.get_dict() for blog_obj in blog_objs]
    print(blog_posts)
    return render_template('index.html', posts=blog_posts, year=year, logged_in=current_user.is_authenticated)


@app.route('/about')
def about_page():
    return render_template('about.html', year=year, logged_in=current_user.is_authenticated)


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        # TODO: Send Mail
        return redirect(url_for('msg_sent_func'))
    return render_template('contact.html', year=year, form=contact_form, logged_in=current_user.is_authenticated)


@app.route('/post/<int:_id>', methods=['GET', 'POST'])
def post_page(_id):
    post = BlogPost.query.get(_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        print(comment_form.comment.data)
        new_comment = Comment(
            text=comment_form.comment.data,
            author=current_user,
            parent_post=post,
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('post_page', _id=_id))
    post_comments = post.comments
    print(post_comments)
    return render_template('post.html', year=year, post=post,
                           logged_in=current_user.is_authenticated, form=comment_form,
                           comments=post_comments)


@app.route("/msg-sent", methods=['GET'])
def msg_sent_func():
    return render_template('msg-sent.html', year=year, logged_in=current_user.is_authenticated)


@app.route("/add", methods=['GET', 'POST'])
@admin_only
def add_func():
    editor_form = PostEditorForm()
    if editor_form.validate_on_submit():
        post_data = editor_form.get_from_data()
        date = get_formatted_date()
        post_data['date'] = date
        post_data['author'] = current_user
        # print(post_data)
        new_post = BlogPost.create_from_dict(data=post_data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index_page'))
    return render_template('make-post.html', year=year, form=editor_form, logged_in=current_user.is_authenticated)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_only
def edit_post(id):
    post = BlogPost.query.get(id)
    # print(f'>>> {post.title}')
    editor_form = PostEditorForm(
        title=post.title,
        subtitle=post.subtitle,
        # author=post.author,
        img_url=post.img_url,
        body=post.body,
    )
    if editor_form.validate_on_submit():
        edited_post_data = editor_form.get_from_data()
        post.title = edited_post_data.get('title')
        post.subtitle = edited_post_data.get('subtitle')
        # post.author = edited_post_data.get('author')
        post.img_url = edited_post_data.get('img_url')
        post.body = edited_post_data.get('body')
        db.session.commit()
        return redirect(url_for('post_page', _id=id))
    return render_template('make-post.html', year=year, form=editor_form, logged_in=current_user.is_authenticated)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@admin_only
def delete_func(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        data = register_form.get_form_data()
        h_pswd = generate_password_hash(
            password=data.get('password'),
            method='pbkdf2:sha256', salt_length=8
        )
        data['password'] = h_pswd
        newusr = User.create_from_dict(data=data)
        try:
            db.session.add(newusr)
            db.session.commit()
            login_user(user=newusr)
            return redirect(url_for('index_page', id=newusr.id))
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()  # https://stackoverflow.com/questions/8870217/why-do-i-get-sqlalchemy-nested-rollback-error
            flash(message='This Email is already Registered, you should login instead.')
            return redirect(url_for('login_page'))

    return render_template('register.html', form=register_form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        data = login_form.get_form_data()
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            if check_password_hash(user.password, data['password']):
                login_user(user=user)
                return redirect(url_for('index_page'))
            else:
                flash('Wrong Password')
        else:
            flash(message='No user with this email.')
    return render_template('login.html', form=login_form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index_page'))


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
