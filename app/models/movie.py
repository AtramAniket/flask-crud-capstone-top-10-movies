from app.extensions import db
from sqlalchemy import Integer, String, Float, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

class Movie(db.Model):

	id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

	title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

	year: Mapped[int] = mapped_column(Integer, nullable=False)

	description: Mapped[str] = mapped_column(String(255), nullable=False)

	rating: Mapped[float] = mapped_column(Numeric(3, 1), nullable=False)

	ranking: Mapped[int] = mapped_column(Integer, nullable=False)

	review: Mapped[str] = mapped_column(Text, nullable=False)

	img_url: Mapped[str] = mapped_column(String(500), nullable=False)


	def __repr__(self):
		return f"<Movie {self.title}>"