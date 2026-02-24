from flask import Blueprint, render_template
from app.extensions import db
from app.models.movie import Movie

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/')
def home():
	return render_template('index.html')


@movies_bp.route('/add')
def add_new_movie():
	return render_template('add.html')


@movies_bp.route('/edit/<int:movie_id>')
def edit_movie(movie_id):
	return render_template('edit.html')