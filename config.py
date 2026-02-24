import os
from dotenv import load_dotenv

# application secrets stored in .emv file
load_dotenv()

class Config:
	"""
		This is the configuration for the flask application
	"""

	SECRET_KEY = os.getenv('APP_SECRET_KEY')

	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

	BOOTSTRAP_BOOTSWATCH_THEME = 'zephyr'