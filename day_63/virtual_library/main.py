from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_book_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'"<{self.id}> {self.title} - {self.author}"'

    def get_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
        }


db.create_all()


@app.route('/')
def home():
    all_book_objs = Book.query.all()
    all_books = [book_obj.get_dict() for book_obj in all_book_objs]
    return render_template('index.html', list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            rating=float(request.form.get('rating'))
        )
        db.session.add(new_book)
        db.session.commit()
    return render_template('add.html')


@app.route('/delete')
def delete():
    book_id = int(request.args.get('id'))
    deletion_book = Book.query.get(book_id)
    db.session.delete(deletion_book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    book_id = request.args['id']
    book = Book.query.get(book_id)
    if request.method == 'POST':
        book.rating = float(request.form.get('new-rating'))
        db.session.commit()
        return redirect(url_for('home'))

    book_info = book.get_dict()
    return render_template('edit.html', info=book_info)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
