from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    # year = StringField("Year Released")
    # description = StringField("Description")
    # rating = FloatField("Rating")
    # ranking = IntegerField("Ranking")
    # review = StringField("Review")
    # img_url = StringField("Image URL")
    submit = SubmitField("Add")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

# Adding the Update functionality
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():

    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    movie_title = request.args.get('title')
    movie_year = request.args.get('year')
    movie_description = request.args.get('description')
    movie_img_url = request.args.get('img_url')
    if movie_title != None:
        new_movie = Movie(
            title = movie_title,
            year = movie_year,
            description = movie_description,
            img_url = f'https://image.tmdb.org/t/p/w500/{movie_img_url}'
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id = new_movie.id))
    titleform = AddMovieForm()

    if titleform.validate_on_submit():
        title = titleform.title.data
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1&region=North%20America"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMjZiNjQ3MDU1NjUyYzhiMTMwNTllNjY4NGQ0ZGFhMSIsInN1YiI6IjY2MTIwYjViMzU2YTcxMDE3ZDI0Yzk0NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.k6TQe9_FpSLNxuoqWW_ReRbL8QfixE5XFW3QgcI4__Y"
        }

        response = requests.get(url, headers=headers).json()
        results = response["results"]

        return render_template("select.html", results = results)
    return render_template("add.html", form = titleform)




if __name__ == '__main__':
    app.run(debug=True)