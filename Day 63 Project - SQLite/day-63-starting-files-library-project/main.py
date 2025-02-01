from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy(app)

# Define the Books model
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String, unique=True)
    author = db.Column(db.String)
    rating = db.Column(db.Integer)

# Define the form for adding books
class Add(FlaskForm):
    book = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Author')
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 11)])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    books = Books.query.all()
    return render_template("index.html", books=books)

@app.route('/add', methods=["GET", "POST"])
def add():
    form = Add()
    if form.validate_on_submit():
        book = Books(
            book=form.book.data,
            author=form.author.data,
            rating=int(form.rating.data)
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Books, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)