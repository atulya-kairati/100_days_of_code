from pprint import pprint
import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from day_64.movie_project.my_forms import EditForm, AddMovieForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

tmdb_img = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(1000), unique=True, nullable=False)

    def __repr__(self):
        return f'"<{self.id}> {self.title} - {self.year}"'

    def get_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "description": self.description,
            "rating": self.rating,
            "review": self.review,
            "img_url": self.img_url,
        }


def search_movies(query):
    tmdb_api = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "08f1cdb1b51b1e061e276faa177f4a43",
        "language": "en-US",
        "query": query,
        "page": 1,
        "include_adult": "false"
    }
    res = requests.get(url=tmdb_api, params=params)
    return res.json().get('results')


@app.route("/")
def home():
    movie_objs = Movie.query.order_by(Movie.rating.desc())
    movies = [movie_obj.get_dict() for movie_obj in movie_objs]
    # print(movies)
    enum_mov = list(enumerate(movies))
    return render_template("index.html", movies=enum_mov)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        movie_query = add_movie_form.movie.data
        all_movies = search_movies(movie_query)
        print(all_movies)
        return render_template('select_movie.html', all_movies=all_movies)
    return render_template('add.html', form=add_movie_form)


@app.route('/save/<movie_id>')
def save(movie_id):
    tmdb_movie_detail_api = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        "api_key": "08f1cdb1b51b1e061e276faa177f4a43",
        "language": "en-US",
    }
    res = requests.get(url=tmdb_movie_detail_api, params=params)
    data = res.json()
    pprint(data)
    new_movie = Movie(
        title=data['title'],
        year=int(data['release_date'].split('-')[0]),
        description=data['overview'],
        rating=0,
        review='None',
        img_url=f'{tmdb_img}{data.get("poster_path")}',
    )
    try:
        db.session.add(new_movie)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        print('Error occured')
        return redirect(url_for('home'))

    mid = Movie.query.filter_by(title=data['title']).first().id
    return redirect(url_for('edit', id=mid))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    movie_id = int(request.args.get('id'))
    edit_form = EditForm()
    movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    movie_title = movie.get_dict()['title']
    return render_template('edit.html', movie_title=movie_title, form=edit_form)


@app.route('/delete')
def delete():
    movie_id = int(request.args['id'])
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
