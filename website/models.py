from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    director = db.Column(db.String(100), nullable=False)
    poster_url = db.Column(db.Text, nullable=False)
    trailer_url = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float(), nullable=True, default=0)
    description = db.Column(db.Text, nullable=False)
    __table_args__ = (
        db.CheckConstraint('0 <= rating & rating <= 10', name='Overall rating should be between 0 and 10'),
        {})
