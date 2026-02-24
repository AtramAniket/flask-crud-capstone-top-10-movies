from flask import Flask
from .routes.movies import movies_bp
from .extensions import db, bootstrap

def create_app():

	app = Flask(__name__)

	app.config.from_object('config.Config')

	db.init_app(app)

	bootstrap.init_app(app)

	app.register_blueprint(movies_bp)

	return app


