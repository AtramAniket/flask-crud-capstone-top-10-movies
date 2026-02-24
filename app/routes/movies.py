from flask import Blueprint, render_template, url_for, redirect
from app.forms.movie_form import MovieForm
from app.extensions import db
from app.models.movie import Movie

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/')
def home():
	movies_list = db.session.scalars(db.select(Movie).order_by(Movie.ranking)).all()
	return render_template('index.html', movies = movies_list)


@movies_bp.route('/add', methods=['GET', 'POST'])
def add_new_movie():
	form = MovieForm()
	form.submit.label.text = 'Add Movie'
	if form.validate_on_submit():
		title = form.title.data
		year = form.year.data
		description = form.description.data
		rating = form.rating.data
		ranking = form.ranking.data
		review = form.review.data
		img_url = form.img_url.data
		movie = Movie(title=title,year=year,description=description,rating=rating,ranking=ranking,review=review,img_url=img_url)
		db.session.add(movie)
		db.session.commit()
		return redirect(url_for('movies.home'))
	return render_template('movie_form.html', form=form, page_title="Add New Movie", form_heading = "Add New Movie")


@movies_bp.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):

	movie = Movie.query.get_or_404(movie_id)
	
	form = MovieForm(obj=movie)

	form.submit.label.text = 'Update'

	if form.validate_on_submit():
		form.populate_obj(movie)
		db.session.add(movie)
		db.session.commit()
		return redirect(url_for('movies.home'))
	return render_template('movie_form.html', form=form, page_title="Edit Movie", form_heading = "Edit Movie")

@movies_bp.route('/delete/<int:movie_id>', methods=['GET','POST'])
def delete_movie(movie_id):
	
	movie = Movie.query.get_or_404(movie_id)
	
	db.session.delete(movie)
	db.session.commit()

	return redirect(url_for('movies.home'))
		