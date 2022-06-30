from flask import Blueprint, jsonify, render_template
from .models import Movie

views = Blueprint('views', __name__)


@views.route('/movies', methods=['GET'], defaults={'movie_id': None})
@views.route('/movies/<movie_id>', methods=['GET'])
def get_movies(movie_id):
    if movie_id:
        try:
            movie_id = int(movie_id)
            movie = Movie.query.filter_by(id=movie_id).first()
            if movie:
                return render_template('movie.html', movie=movie)
            return jsonify({'message': 'Movie not found'}), 404
        except ValueError:
            return jsonify({'message': 'Invalid movie id'}), 400
        except:
            return jsonify({'message': 'Bad gateway'}), 502

    return render_template('index.html', movies=Movie.query.all(), len=len(Movie.query.all()))


@views.route('api/movies', methods=['GET'], defaults={'movie_id': None})
@views.route('api/movie/<movie_id>', methods=['GET'])
def get_movies_api(movie_id):

    def row_to_dict(row):
        return {c.name: str(getattr(row, c.name)) for c in row.__table__.columns}

    if movie_id:
        try:
            movie_id = int(movie_id)
            movie = Movie.query.filter_by(id=movie_id).first()
            if movie:
                return jsonify(row_to_dict(movie)), 200
            return jsonify({'message': 'Movie not found'}), 404
        except ValueError:
            return jsonify({'message': 'Invalid movie id'}), 400
        except:
            return jsonify({'message': 'Bad gateway'}), 502

    return jsonify({'movies': [row_to_dict(movie) for movie in Movie.query.all()]}), 200


@views.route('/', methods=['GET'])
def home():
    return get_movies(None)
