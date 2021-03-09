from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    hashed_pw = db.Column(db.String(160))
    name = db.Column(db.String(1000))


#Line below only required once, when creating DB. 
# db.create_all()

# user loader for FLask Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    # print(current_user.id)
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        creds = request.form
        name = creds.get('name')
        password = creds.get('password')
        hashed_pw = generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8)
        email = creds.get('email')
        newusr = User(name=name, email=email, hashed_pw=hashed_pw)
        try:
            db.session.add(newusr)
            db.session.commit()
            login_user(user=newusr)
            return redirect(url_for('secrets', id=newusr.id))
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()  # https://stackoverflow.com/questions/8870217/why-do-i-get-sqlalchemy-nested-rollback-error
            flash(message='This Email is already Registered, you should login instead.')
            return redirect(url_for('login'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(pwhash=user.hashed_pw, password=password):
                login_user(user=user)
                return redirect(url_for('secrets', id=user.id))
            else:
                flash(message="You entered Wrong password.")
        else:
            flash(message='This Email has not been registered yet..')
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(request.args)
    id = request.args.get('id')
    name = current_user.name
    # user = User.query.get(id)
    # name = user.name
    return render_template("secrets.html", name=name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
